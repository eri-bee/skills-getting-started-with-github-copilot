document.addEventListener("DOMContentLoaded", () => {
  const activitiesList = document.getElementById("activities-list");
  const activitySelect = document.getElementById("activity");
  const signupForm = document.getElementById("signup-form");
  const messageDiv = document.getElementById("message");

  // Function to fetch activities from API
  async function fetchActivities() {
    try {
      const response = await fetch("/activities");
      const activities = await response.json();

      // Clear loading message
      activitiesList.innerHTML = "";
      // Reset activity select to avoid duplicate options
      activitySelect.innerHTML = '<option value="">-- Select an activity --</option>';

      // Populate activities list
      Object.entries(activities).forEach(([name, details]) => {
        const activityCard = document.createElement("div");
        activityCard.className = "activity-card";

        const spotsLeft = details.max_participants - details.participants.length;

        activityCard.innerHTML = `
          <h4>${name}</h4>
          <p>${details.description}</p>
          <p><strong>Schedule:</strong> ${details.schedule}</p>
          <p><strong>Availability:</strong> ${spotsLeft} spots left</p>
        `;

        // Participants section (added dynamically for safety)
        const participantsSection = document.createElement('div');
        participantsSection.className = 'participants-section';

        const participantsTitle = document.createElement('h5');
        participantsTitle.textContent = 'Participants';
        participantsSection.appendChild(participantsTitle);

        const participantsListEl = document.createElement('ul');
        participantsListEl.className = 'participants-list';

        if (details.participants && details.participants.length > 0) {
          details.participants.forEach((p) => {
            const li = document.createElement('li');
            li.className = 'participant-row';

            const nameSpan = document.createElement('span');
            nameSpan.textContent = p;
            nameSpan.className = 'participant-name';

            const deleteBtn = document.createElement('button');
            deleteBtn.type = 'button';
            deleteBtn.className = 'participant-delete';
            deleteBtn.setAttribute('aria-label', `Remove ${p}`);
            deleteBtn.textContent = '✖';

            deleteBtn.addEventListener('click', async () => {
              const confirmRemove = confirm(`Remove ${p} from ${name}?`);
              if (!confirmRemove) return;

              try {
                const res = await fetch(`/activities/${encodeURIComponent(name)}/unregister?email=${encodeURIComponent(p)}`, {
                  method: 'POST',
                });

                const resJson = await res.json().catch(() => ({}));

                if (res.ok) {
                  // Refresh activities list to reflect removal
                  fetchActivities();

                  // show brief success message
                  if (messageDiv) {
                    messageDiv.textContent = resJson.message || 'Participant removed';
                    messageDiv.className = 'message success';
                    messageDiv.classList.remove('hidden');
                    setTimeout(() => messageDiv.classList.add('hidden'), 4000);
                  }
                } else {
                  if (messageDiv) {
                    messageDiv.textContent = resJson.detail || 'Failed to remove participant';
                    messageDiv.className = 'message error';
                    messageDiv.classList.remove('hidden');
                  }
                }
              } catch (err) {
                console.error('Error removing participant:', err);
                if (messageDiv) {
                  messageDiv.textContent = 'Failed to remove participant';
                  messageDiv.className = 'message error';
                  messageDiv.classList.remove('hidden');
                }
              }
            });

            li.appendChild(nameSpan);
            li.appendChild(deleteBtn);

            participantsListEl.appendChild(li);
          });
        } else {
          const li = document.createElement('li');
          li.textContent = 'No participants yet';
          li.className = 'empty';
          participantsListEl.appendChild(li);
        }

        participantsSection.appendChild(participantsListEl);

        activitiesList.appendChild(activityCard);
        activityCard.appendChild(participantsSection);

        // Add option to select dropdown
        const option = document.createElement("option");
        option.value = name;
        option.textContent = name;
        activitySelect.appendChild(option);
      });
    } catch (error) {
      activitiesList.innerHTML = "<p>Failed to load activities. Please try again later.</p>";
      console.error("Error fetching activities:", error);
    }
  }

  // Handle form submission
  signupForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const activity = document.getElementById("activity").value;

    try {
      const response = await fetch(
        `/activities/${encodeURIComponent(activity)}/signup?email=${encodeURIComponent(email)}`,
        {
          method: "POST",
        }
      );

      const result = await response.json();

      if (response.ok) {
        messageDiv.textContent = result.message;
        messageDiv.className = "message success";
        signupForm.reset();
        // Refresh activities list to show updated participant count
        fetchActivities();
      } else {
        messageDiv.textContent = result.detail || "An error occurred";
        messageDiv.className = "message error";
      }

      messageDiv.classList.remove("hidden");

      // Hide message after 5 seconds
      setTimeout(() => {
        messageDiv.classList.add("hidden");
      }, 5000);
    } catch (error) {
      messageDiv.textContent = "Failed to sign up. Please try again.";
      messageDiv.className = "error";
      messageDiv.classList.remove("hidden");
      console.error("Error signing up:", error);
    }
  });

  // Initialize app
  fetchActivities();
});
