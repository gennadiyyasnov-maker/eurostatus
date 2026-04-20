import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_h1 = """<!-- Morphing Hero Title -->
<h1 style="position: relative; display: flex; flex-direction: column; gap: 10px;">
  <div style="display: flex; flex-wrap: wrap; gap: 12px; align-items: baseline;">
    <span>Паспорт</span>
    <span class="morphing-country">Евросоюза</span>
  </div>
  <span>за 5-12 месяцев</span>
</h1>
<style>
  .morphing-country {
    display: inline-block;
    color: #c9a050; 
    border-bottom: 3px solid #c9a050;
    transition: opacity 0.5s ease, transform 0.5s ease, width 0.5s ease;
    text-align: left;
    white-space: nowrap;
  }
  .morphing-country.fade-out {
    opacity: 0;
    transform: translateY(-10px) rotateX(10deg);
  }
  .morphing-country.fade-in {
    opacity: 0;
    transform: translateY(10px) rotateX(-10deg);
  }
</style>
<script>
  document.addEventListener("DOMContentLoaded", () => {
    const countries = ["Евросоюза", "Румынии", "Болгарии", "Словении", "Польши", "Армении", "Испании"];
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
</script>
<!-- End Morphing Title -->"""

content = re.sub(r'<h1>Паспорт Евросоюза за 5-12 месяцев</h1>', new_h1, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
