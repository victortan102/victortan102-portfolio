console.log("resume.js loaded");

document.addEventListener("DOMContentLoaded", () => {
    const list = document.getElementById("workExperienceList");
    const toggleBtn = document.getElementById("workExperienceToggle");

    if (!list || !toggleBtn) return;

    const items = Array.from(list.querySelectorAll(".resume-item"));
    const COLLAPSE_COUNT = 3;

    // If 3 or fewer, no need to collapse
    if (items.length <= COLLAPSE_COUNT) {
        toggleBtn.style.display = "none";
        list.style.maxHeight = "none";
        return;
    }

    // Helper: compute height up to N items
    function heightUpToN(n) {
        let h = 0;
        for (let i = 0; i < n; i++) {
            h += items[i].offsetHeight;
            // Include margin-bottom if any (common in resume templates)
            const style = window.getComputedStyle(items[i]);
            h += parseFloat(style.marginBottom || "0");
            h += parseFloat(style.marginTop || "0");
        }
        return h;
    }

    // Collapsed/expanded heights
    const collapsedHeight = heightUpToN(COLLAPSE_COUNT);

    // Start collapsed
    let expanded = false;
    list.classList.add("is-collapsed");
    list.style.maxHeight = collapsedHeight + "px";
    toggleBtn.textContent = "View more";

    toggleBtn.addEventListener("click", () => {
        expanded = !expanded;

        if (expanded) {
            // Expand fully
            list.classList.remove("is-collapsed");
            list.style.maxHeight = list.scrollHeight + "px";
            toggleBtn.textContent = "View less";
        } else {
            // Collapse back
            list.classList.add("is-collapsed");
            list.style.maxHeight = collapsedHeight + "px";
            toggleBtn.textContent = "View more";

            // Optional: scroll back to top of work exp so user doesn't feel "lost"
            list.scrollIntoView({ behavior: "smooth", block: "start" });
        }

        // If you use AOS animations, refreshing can help after expanding
        if (window.AOS && typeof window.AOS.refresh === "function") {
            window.AOS.refresh();
        }
    });

    // If images load later (icons/logos) and change heights, recalc after load
    window.addEventListener("load", () => {
        const newCollapsedHeight = heightUpToN(COLLAPSE_COUNT);
        if (!expanded) list.style.maxHeight = newCollapsedHeight + "px";
    });
});
