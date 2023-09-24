function useState(initialValue) {
  let state = initialValue; // Initialize the state with the provided initial value

  // Define a setter function to update the state
  function setState(newValue) {
    state = newValue;
  }

  // Return an array containing the current state and the setter function
  return [state, setState];
}

const [data, setData] = useState('');

function myNavigation(page) {
  window.location.href = page;
}

const deleteStudent = (studentId) => {
  fetch("/users/" + studentId, {
    method: "DELETE",
  }).then((_res) => {
    window.location.href = "/users";
  });
};

async function fetchData() {
  try {
    const response = await fetch("/current-user");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    username = document.getElementById("username");
    username.textContent = data.username;

    console.log(data);
  } catch (error) {
    console.error("Fetch error:", error);
  }
}

fetchData();


  