const API = (() => {
    const host = window.location.hostname;

    if (host === "localhost" || host === "127.0.0.1") {
        return "http://127.0.0.1:8000";
    }

    return "https://fixit-backend-x2f1.onrender.com";
})();