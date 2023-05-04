function validateForm() {
    var name = document.forms["signupForm"]["name"].value;
    var email = document.forms["signupForm"]["email"].value;
    var password = document.forms["signupForm"]["password"].value;
    
    console.log("Name: " + name);
    console.log("Email: " + email);
    console.log("Password: " + password);
    
    if (name == "" || email == "" || password == "") {
      alert("Name, email, and password fields must be filled out");
      return false;
    }
    return true;
  }

