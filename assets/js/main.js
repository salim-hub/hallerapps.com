document.addEventListener("DOMContentLoaded", () => {
    // 1. Navbar Active Link Highlight
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll(".navbar nav a");
    navLinks.forEach(link => {
        const href = link.getAttribute("href");
        // Check exact match or sub-directory match, while avoiding matching '/' to everything
        if (href === currentPath || (currentPath.startsWith(href) && href !== "/")) {
            link.classList.add("active");
        }
    });

    // 2. Mobile Hamburger Menu Toggle
    const navbar = document.querySelector(".navbar");
    if (navbar) {
        const container = navbar.querySelector(".container");
        // Create hamburger button dynamically if it doesn't exist
        let hamburger = document.querySelector(".hamburger-menu");
        if (!hamburger) {
            hamburger = document.createElement("button");
            hamburger.className = "hamburger-menu";
            hamburger.setAttribute("aria-label", "Toggle Menu");
            hamburger.innerHTML = `
                <span></span>
                <span></span>
                <span></span>
            `;
            container.appendChild(hamburger);
        }

        const nav = navbar.querySelector("nav");
        hamburger.addEventListener("click", () => {
            hamburger.classList.toggle("open");
            nav.classList.toggle("open");
        });
    }

    // 3. Scroll Reveal Animations (Intersection Observer)
    const revealElements = document.querySelectorAll(".reveal");
    if (revealElements.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("active");
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: "0px 0px -50px 0px"
        });

        revealElements.forEach(el => observer.observe(el));
    }

    // 4. Privacy Page Tab Switcher
    const tabBtns = document.querySelectorAll(".tab-btn");
    const tabContents = document.querySelectorAll(".tab-content");

    if (tabBtns.length > 0 && tabContents.length > 0) {
        tabBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                const targetTab = btn.getAttribute("data-tab");

                // Remove active classes
                tabBtns.forEach(b => b.classList.remove("active"));
                tabContents.forEach(c => c.classList.remove("active"));

                // Add active class to clicked button and target tab content
                btn.classList.add("active");
                const targetContent = document.getElementById(targetTab);
                if (targetContent) {
                    targetContent.classList.add("active");
                }
            });
        });
    }
});
