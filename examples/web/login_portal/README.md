Login Portal
===

This is an example of a **static** challenge.

## Summary
* **Author:** Zavier Lee
* **Discord Tag:** gatari#9922
* **Category:** Web 
* **Difficulty:** Easy

## Solution
1. Visit the website, you are greeted with a login page.
2. View page source and locate the script tag, and read the source of `login.js`.
```js
const login = () => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    if (username === "alden.chia" && password === "password123") {
        const token = btoa("admin:password123");
        document.cookie = "token=" + token;
        window.location.href = "admin.html";
    } else {
        alert("Invalid username or password");
    }
}
```
3. The username and password is `alden.chia` and `password123` respectively, as given by the source code.
4. Login with the credentials, and you will be redirected to `admin.html`.

## Flag
```
YCEP2023{4ld3N_cH14_IS_S0_C0ol}
```

## Additional Notes
* `admin.js` can be ignored, the purpose of this script is to prevent users from redirecting directly to `admin.html` without logging in.
```js
if (name === "token") {
    const token = atob(value);
    if (token === "admin:password123") {
        return true;
    } else {
        break;
    }
}
```

