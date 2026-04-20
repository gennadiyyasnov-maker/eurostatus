with open('assets/js/main.js', 'a', encoding='utf-8') as f:
    f.write("""

// Morphing Hero Country Animation
document.addEventListener("DOMContentLoaded", () => {
  const countries = ["Евросоюза", "Румынии", "Болгарии", "Словении", "Польши", "Турции", "Австрии", "Израиля", "Германии", "Венгрии", "Армении", "Испании"];
  let currentIndex = 0;
  const morphEl = document.querySelector(".morphing-country");
  
  if(morphEl) {
    setInterval(() => {
      morphEl.classList.add("fade-out");
      
      setTimeout(() => {
        currentIndex = (currentIndex + 1) % countries.length;
        morphEl.textContent = countries[currentIndex];
        
        morphEl.classList.remove("fade-out");
        morphEl.classList.add("fade-in");
        
        // force reflow
        void morphEl.offsetWidth;
        
        morphEl.classList.remove("fade-in");
      }, 500); 
    }, 3500); 
  }
});
""")
