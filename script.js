document.addEventListener("DOMContentLoaded", () => {
    const tocContainer = document.getElementById("toc-container");
    const contentContainer = document.getElementById("content-container");

    dsaData.forEach((section, index) => {
        // Build TOC Link
        const tocLink = document.createElement("a");
        tocLink.href = `#section-${index}`;
        tocLink.style.setProperty("--tab-color", section.color);
        tocLink.textContent = section.title;
        tocContainer.appendChild(tocLink);

        // Build Section
        const sectionEl = document.createElement("section");
        sectionEl.className = "category";
        sectionEl.id = `section-${index}`;
        sectionEl.style.setProperty("--cat-color", section.color);

        const headerEl = document.createElement("div");
        headerEl.className = "section-header";
        headerEl.innerHTML = `<span class="label">${index + 1}</span><span class="sub">${section.title}</span>`;
        sectionEl.appendChild(headerEl);

        const gridEl = document.createElement("div");
        gridEl.className = "grid";

        // Build Cards
        section.patterns.forEach((pattern, pIndex) => {
            const cardId = `card-${index}-${pIndex}`;
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
            cardEl.appendChild(mentalModelEl);

            // Problem Links
            if (pattern.problems && pattern.problems.length > 0) {
                const linksEl = document.createElement("div");
                linksEl.className = "problem-links";
                linksEl.innerHTML = `<b>Practice:</b> ` + pattern.problems.map(p => `<a href="${p.url}" target="_blank">${p.name}</a>`).join("");
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
});
