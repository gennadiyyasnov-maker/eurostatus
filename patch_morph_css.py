with open('assets/css/style.css', 'a', encoding='utf-8') as f:
    f.write("""

/* Morphing Hero */
.morphing-country {
  display: inline-block;
  color: #c9a050 !important;
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
""")
