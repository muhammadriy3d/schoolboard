function isUpperCase(text) {
  return text === text.toUpperCase();
}

(() => {
  "use strict";

  const forms = document.querySelectorAll(".needs-validation");
  const patterns = {
    username: /^((?![_-])[a-z0-9]{3,})(?:[a-z0-9.%+]*[a-z0-9])?(?<![_-])$/,
    email:
      /^[a-zA-Z0-9](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])+@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z]{2,})+$/,
    password:
      /^((?=.*?[#?!@$%^&*-])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[a-z])).{8,24}$/i,
  };

  forms.forEach((form) => {
    form.addEventListener("keyup", (e) => {
      function validate(field, regex) {
        if (field.attributes.id.value === "confirmation") {
          if (
            form.password.value === form.confirmation.value ||
            form.confirmation.value === form.password.value
          ) {
            $("#confirmationNotMatchFeedback").text("");
            $("#confirmationMatchFeedback").text("Passwords match!");
            form.confirmation.className = "form-control text-lg is-valid";
            return form.confirmation.classList.add("was-validated");
          }
        } else {
          return regex.test(field.value);
        }
        return e.target.classList.add("was-validated");
      }

      if (validate(e.target, patterns[e.target.attributes.id.value])) {
        e.target.className = "form-control text-lg is-valid";
        e.target.classList.add("was-validated");
      } else {
        e.target.className = "form-control text-lg is-invalid";
        e.target.classList.add("was-validated");
      }
    });
  });

  window.addEventListener(
    "load",
    () => {
      Array.from(forms).forEach((form) => {
        const f1 = form.username;
        const f2 = form.email;
        const f3 = form.password;
        const f4 = form.confirmation;

        form.addEventListener("submit", (event) => {
          if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
          }

          form.classList.add("was-validated");
        });

        // f1.addEventListener("input", (event) => {
        //   let checkx = true;
        //   let chr = String.fromCharCode(event.which);

        //   const usernamePattern = /^((?![_-])[a-z0-9]{3,})(?:[a-z0-9.%+]*[a-z0-9])?(?<![_-])$/

        //   if (new RegExp(usernamePattern[i]).test(f1.value)) {
        //       checkx = false;
        //   }

        //   if (f1.value.length >= 12) checkx = true;

        //   if (checkx) {
        //     event.preventDefault();
        //     event.stopPropagation();
        //   }
        // });

        f3.addEventListener("input", (event) => {
          let checkx = true;
          let chr = String.fromCharCode(event.which);

          const passwordPattern = [
            "(?=.*?[#?!@$%^&*-])",
            "(?=.*?[A-Z])",
            "(?=.*?[0-9])",
            "(?=.*?[a-z])",
          ];

          for (let i = 0; i < passwordPattern.length; i++) {
            if (new RegExp(passwordPattern[i]).test(chr)) {
              checkx = false;
            }
          }

          if (f3.value.length >= 24) checkx = true;

          if (checkx) {
            event.preventDefault();
            event.stopPropagation();
          }
        });

        f3.addEventListener("keyup", () => {
          const passwordPattern = [
            "(?=.*?[#?!@$%^&*-])",
            "(?=.*?[A-Z])",
            "(?=.*?[0-9])",
            "(?=.*?[a-z])",
          ];

          let messageCase = [
            " Special Character",
            " Upper Case",
            " Numbers",
            " Lower Case",
          ];

          let ctr = 0;

          for (let i = 0; i < passwordPattern.length; i++) {
            if (new RegExp(passwordPattern[i]).test(f3.value)) {
              messageCase.splice(i, 1);
              ctr++;
            }
          }

          let sometext = "";

          if (f3.value.length < 8) {
            let lengthI = 8 - f3.value.length;
            sometext += ` ${lengthI} more Characters, `;
          }

          sometext += messageCase.join(", ");

          if (sometext) {
            sometext = " You Need" + sometext;
          }

          $("#invalidFeedback").text(sometext);

          let progressbar = 0;
          let strength = "";
          let bClass = "";

          switch (ctr) {
            case 0:
            case 1:
              strength = "Way too Weak";
              progressbar = 15;
              bClass = "bg-danger";
              break;
            case 2:
              strength = "Very Weak";
              progressbar = 25;
              bClass = "bg-danger";
              break;
            case 3:
              strength = "Weak";
              progressbar = 34;
              bClass = "bg-warning";
              break;
            case 4:
              strength = "Medium";
              progressbar = 65;
              bClass = "bg-warning";
              break;
          }

          if (strength == "Medium" && f3.value.length >= 8) {
            strength = "Strong";
            bClass = "bg-success";
            $("#validFeedback").text("Strong");
            f3.setCustomValidity("");
          } else {
            f3.setCustomValidity(strength);
          }

          let plength = f3.value.length;
          if (plength > 0) progressbar += (plength - 0) * 1.75;
          let percentage = progressbar + "%";
          f3.parentNode.classList.add("was-validated");
          $("#progressbar")
            .removeClass("bg-danger bg-warning bg-success")
            .addClass(bClass);
          $("#progressbar").width(percentage);
        });

        const passwordPattern = [
          "(?=.*?[#?!@$%^&*-])",
          "(?=.*?[A-Z])",
          "(?=.*?[0-9])",
          "(?=.*?[a-z])",
        ];

        f4.addEventListener("input", (event) => {
          let checkx = true;
          let chr = String.fromCharCode(event.which);

          for (let i = 0; i < passwordPattern.length; i++) {
            if (new RegExp(passwordPattern[i]).test(chr)) {
              checkx = false;
            }
          }

          if (f4.value.length >= 24) checkx = true;

          if (checkx) {
            event.preventDefault();
            event.stopPropagation();
          }
        });

        f4.addEventListener("keyup", () => {
          let messageCase = [
            " Special Character",
            " Upper Case",
            " Numbers",
            " Lower Case",
          ];

          let ctr = 0;

          for (let i = 0; i < passwordPattern.length; i++) {
            if (new RegExp(passwordPattern[i]).test(f4.value)) {
              messageCase.splice(i, 1);
              ctr++;
            }
          }

          let sometext = "";

          if (f4.value.length < 8) {
            let lengthI = 8 - f4.value.length;
            sometext += ` ${lengthI} more Characters, `;
          }

          sometext += messageCase.join(", ");

          let progressbar = 0;
          let strength = "";
          let bClass = "";

          switch (ctr) {
            case 0:
            case 1:
              strength = "Way too Weak";
              progressbar = 15;
              bClass = "bg-danger";
              break;
            case 2:
              strength = "Very Weak";
              progressbar = 25;
              bClass = "bg-danger";
              break;
            case 3:
              strength = "Weak";
              progressbar = 34;
              bClass = "bg-warning";
              break;
            case 4:
              strength = "Medium";
              progressbar = 65;
              bClass = "bg-warning";
              break;
          }

          if (
            strength == "Medium" &&
            f4.value.length >= 8 &&
            f4.value === f3.value
          ) {
            strength = "Strong";
            bClass = "bg-success";
            f4.setCustomValidity("");
            $("#validFeedback").text("");
            $("#confirmationMatchFeedback").text("Passwords match!");
            f4.parentNode.classList.add("was-validated");
          } else {
            f4.setCustomValidity(strength);
            $("#confirmationMatchFeedback").text("");
            $("#confirmationNotMatchFeedback").text("Passwords do not match!");
          }

          let plength = f4.value.length;
          if (plength > 0) progressbar += (plength - 0) * 1.75;
          let percentage = progressbar + "%";
          $("#confirmProgressbar")
            .removeClass("bg-danger bg-warning bg-success")
            .addClass(bClass);
          $("#confirmProgressbar").width(percentage);
        });
      });
    },
    false
  );
})();
