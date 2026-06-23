document.addEventListener("DOMContentLoaded", () => {
    const tocContainer = document.getElementById("toc-container");
    const contentContainer = document.getElementById("content-container");

    // "Show All" Button
    const showAllBtn = document.createElement("button");
    showAllBtn.style.setProperty("--tab-color", "#333");
    showAllBtn.textContent = "Show All Topics";
    showAllBtn.className = "active-filter";
    showAllBtn.onclick = () => filterSections(null, showAllBtn);
    tocContainer.appendChild(showAllBtn);

    const sectionElements = [];
    const filterButtons = [showAllBtn];

    dsaData.forEach((section, index) => {
        // Build TOC Link/Button
        const tocBtn = document.createElement("button");
        tocBtn.style.setProperty("--tab-color", section.color);
        tocBtn.textContent = section.title;
        tocBtn.onclick = () => filterSections(index, tocBtn);
        tocContainer.appendChild(tocBtn);
        filterButtons.push(tocBtn);

        // Build Section
        const sectionEl = document.createElement("section");
        sectionEl.className = "category";
        sectionEl.id = `section-${index}`;
        sectionEl.style.setProperty("--cat-color", section.color);
        sectionElements.push({ el: sectionEl, index: index });

        const headerEl = document.createElement("div");
        headerEl.className = "section-header";
        headerEl.innerHTML = `<span class="label">${index + 1}</span><span class="sub">${section.title}</span>`;
        sectionEl.appendChild(headerEl);

        const gridEl = document.createElement("div");
        gridEl.className = "grid";

        // Build Cards
        section.patterns.forEach((pattern, pIndex) => {
            const cardEl = document.createElement("div");
            cardEl.className = "card";

            // Title
            const titleEl = document.createElement("h3");
            titleEl.textContent = pattern.name;
            cardEl.appendChild(titleEl);

            // Mental Model & Recognition
            const mentalModelEl = document.createElement("div");
            mentalModelEl.className = "mental-model";
            mentalModelEl.innerHTML = `
                <div><b>When to use:</b> ${pattern.recognition}</div>
                <div><b>Model:</b> ${pattern.mentalModel}</div>
            `;
            if (pattern.pitfalls) {
                mentalModelEl.innerHTML += `<div><b>⚠️ Pitfalls:</b> ${pattern.pitfalls}</div>`;
            }
            cardEl.appendChild(mentalModelEl);

            // Problem Links (Multiple)
            if (pattern.problems && pattern.problems.length > 0) {
                const linksEl = document.createElement("div");
                linksEl.className = "problem-links";
                linksEl.innerHTML = `<b>Practice:</b> ` + pattern.problems.map(p => 
                    `<a href="${p.url}" target="_blank" style="--cat-color: ${section.color}">#${p.num} ${p.name}</a>`
                ).join("");
                cardEl.appendChild(linksEl);
            }

            // Code Tabs
            const codeContainer = document.createElement("div");
            codeContainer.className = "code-container";

            const tabsEl = document.createElement("div");
            tabsEl.className = "tabs";
            
            const preEl = document.createElement("pre");
            const codeEl = document.createElement("code");
            preEl.appendChild(codeEl);

            const languages = Object.keys(pattern.code);
            languages.forEach((lang, lIndex) => {
                const btn = document.createElement("button");
                btn.className = `tab-btn ${lIndex === 0 ? "active" : ""}`;
                btn.textContent = lang;
                btn.onclick = () => {
                    // Remove active from all siblings
                    Array.from(tabsEl.children).forEach(c => c.classList.remove("active"));
                    btn.classList.add("active");
                    codeEl.textContent = pattern.code[lang];
                };
                tabsEl.appendChild(btn);

                // Set initial code to first language
                if (lIndex === 0) {
                    codeEl.textContent = pattern.code[lang];
                }
            });

            codeContainer.appendChild(tabsEl);
            codeContainer.appendChild(preEl);
            cardEl.appendChild(codeContainer);

            gridEl.appendChild(cardEl);
        });

        sectionEl.appendChild(gridEl);
        contentContainer.appendChild(sectionEl);
    });

    // Filtering Logic
    function filterSections(targetIndex, clickedBtn) {
        // Update active class on buttons
        filterButtons.forEach(btn => btn.classList.remove("active-filter"));
        clickedBtn.classList.add("active-filter");

        // Hide/Show sections
        sectionElements.forEach(item => {
            if (targetIndex === null || item.index === targetIndex) {
                item.el.classList.remove("hidden");
            } else {
                item.el.classList.add("hidden");
            }
        });
    }
});
