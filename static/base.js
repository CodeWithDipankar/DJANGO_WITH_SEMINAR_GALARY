// <!-- For validation of password field  -->
function validatePassword() {
    var password = document.getElementById('password').value
    var confirmPassword = document.getElementById('confirm-password').value
    var submitButton = document.getElementById('submit-button')
    const passwordError = document.getElementById('passwordError')
    const passwordError1 = document.getElementById('passwordError1')

    var passwordcolor = document.getElementById('password')

    var uppercaseRegex = /[A-Z]/
    var lowercaseRegex = /[a-z]/
    var numberRegex = /[0-9]/
    var specialRegex = /[#?!@$%^&*-]/

    if (password.length > 0 && password.length <= 15) {
        submitButton.disabled = true
        passwordcolor.className = 'form-control border-danger'
        passwordcolor.classList.add('focus')

        if (password.length < 2) {
            submitButton.disabled = true
            passwordError.textContent = 'Password must contain at least 8 characters,including 1 uppercase letter, 1 lowercase letter, 1 number and 1 special character.'
            return false
        } else if (password.length <= 15) {
            if (!uppercaseRegex.test(password)) {
                submitButton.disabled = true
                passwordError.textContent = 'Password must contain at least 1 uppercase letter.'
                return false
            }
            if (!lowercaseRegex.test(password)) {
                submitButton.disabled = true
                passwordError.textContent = 'Password must contain at least 1 lowercase letter.'
                return false
            }
            if (!numberRegex.test(password)) {
                submitButton.disabled = true
                passwordError.textContent = 'Password must contain at least 1 number and 1 special character'
                return false
            }
            if (!specialRegex.test(password)) {
                submitButton.disabled = true
                passwordError.textContent = 'Password must contain at least 1 special character'
                return false
            }
            if (password.length < 8) {
                submitButton.disabled = true
                passwordError.textContent = 'Password must contain at least 8 characters.'
                return false
            }
            if (uppercaseRegex.test(password) && lowercaseRegex.test(password) && numberRegex.test(password) && specialRegex.test(password) && (password.length >= 8 || password.length <= 15)) {
                passwordcolor.className = 'form-control border-success'
                passwordcolor.classList.add('focus')
                submitButton.disabled = false
                passwordError.textContent = ''
                return true
            }
        }
    } else if (password.length > 15) {
        passwordcolor.className = 'form-control border-danger'
        passwordcolor.classList.add('focus')
        submitButton.disabled = true
        passwordError.textContent = 'Password must be less than 15 characters.'
        return false
    } else {
        passwordcolor.className = 'form-control '
        passwordcolor.classList.add('focus')
        submitButton.disabled = false
        passwordError.textContent = ''
        return false
    }
}

// for valiadtion of password and confirm password-----------------

function validatePassword1() {
    var password = document.getElementById('password').value
    var confirmPassword = document.getElementById('confirm-password').value
    var submitButton = document.getElementById('submit-button')
    const passwordError1 = document.getElementById('passwordError1')

    var confirmPasswordcolor = document.getElementById('confirm-password')

    if (password != confirmPassword && confirmPassword.length > 0) {
        confirmPasswordcolor.className = 'form-control border-danger'
        confirmPasswordcolor.classList.add('focus')
        submitButton.disabled = true
        passwordError1.textContent = 'Password and confirm password does not match'
        return
    } else if (password === confirmPassword && confirmPassword.length > 0 && validatePassword() == true) {
        confirmPasswordcolor.className = 'form-control border-success'
        confirmPasswordcolor.classList.add('focus')
        submitButton.disabled = false
        passwordError1.textContent = ''
        return
    } else if (validatePassword() != true && confirmPassword.length > 0) {
        confirmPasswordcolor.className = 'form-control border-danger'
        confirmPasswordcolor.classList.add('focus')
        submitButton.disabled = true
        passwordError1.textContent = 'Please satisfy the criteria of password field.'
        return
    } else {
        confirmPasswordcolor.className = 'form-control '
        confirmPasswordcolor.classList.add('focus')
        submitButton.disabled = false
        passwordError1.textContent += ''
        return
    }
}

// username validation function only alphabet------
function validateUsername(event) {
    var error = event.id + 'Error'
    var regName = /^[A-Za-z]+$/
    var submitButton = document.getElementById('submit-button')
    var name = document.getElementById(event.id).value
    const usernameError = document.getElementById(error)

    var namecolor = document.getElementById(event.id)

    if (!regName.test(name) && name.length > 0) {
        namecolor.className = 'form-control border-danger'
        namecolor.classList.add('focus')
        usernameError.textContent = '*Please enter a valid name.'
        submitButton.disabled = true
        return
    } else if (regName.test(name) && name.length > 0) {
        namecolor.className = 'form-control border-success'
        namecolor.classList.add('focus')
        usernameError.textContent = ''
        submitButton.disabled = false
    } else {
        namecolor.className = 'form-control'
        namecolor.classList.add('focus')
        usernameError.textContent = ''
        submitButton.disabled = false
        return
    }
}

// For validation of email ----------------
function validateEmail() {
    var regName = /[a-z0-9]+@[a-z]+\.[a-z]{2,3}/
    var email = document.getElementById('email').value
    var submitButton = document.getElementById('submit-button')
    const usernameError = document.getElementById('emailError')

    var emailcolor = document.getElementById('email')

    if (!regName.test(email) && email.length > 0) {
        emailcolor.className = 'form-control border-danger'
        emailcolor.classList.add('focus')
        usernameError.textContent = '*Please enter a valid email address.'
        submitButton.disabled = true
        return
    } else if (regName.test(email) && email.length > 0) {
        emailcolor.className = 'form-control border-success'
        emailcolor.classList.add('focus')
        usernameError.textContent = ''
        submitButton.disabled = false
    } else {
        emailcolor.className = 'form-control'
        emailcolor.classList.add('focus')
        usernameError.textContent = ''
        submitButton.disabled = false
        return
    }
}

function myFunction(evnt) {
    var x = document.getElementById('password')
    var y = document.getElementById('confirm-password')

    if (x.type === 'password') {
        x.type = 'text'
        y.type = 'text'
    } else {
        x.type = 'password'
        y.type = 'password'
    }
}


