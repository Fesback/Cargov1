// data local (mock)
const packagesMock = [
    { id: "P01", name: "Laptops", weight: 10, value: 60},
    { id: "P02", name: "Celulares", weight: 20, value: 100},
    { id: "P03", name: "Monitores", weight: 30, value: 120},
    { id: "P04", name: "Teclados", weight: 15, value: 50}
];

async function ejecutarOptimizacion() {
    const capacityInput = document.getElementById("capacityInput").value;
    const payload = {
        packages: packagesMock,
        capacity: parseInt(capacityInput)
    };

    try {
        const API_URL = "https://intellicargo-backend.onrender.com/optimize";
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error("Error en el servidor o payload incorrecto");
        
        const data = await response.json();

        document.getElementById("resultsSection").classList.remove("hidden");

        document.getElementById("dpValue").innerText = "$" + data.dynamic_programming.value;
        document.getElementById("dpWeight").innerText = data.dynamic_programming.weight + " kg";
        document.getElementById("dpItems").innerHTML = data.dynamic_programming.items.map(i => `<li>${i.name} (${i.weight}kg)</li>`).join("");
        document.getElementById("greedyValue").innerText = "$" + data.greedy.value;
        document.getElementById("greedyWeight").innerText = data.greedy.weight + " kg";
        document.getElementById("greedyItems").innerHTML = data.greedy.items.map(i => `<li>${i.name} (${i.weight}kg)</li>`).join("");

    } catch (error) {
        console.error("Error completo:", error);
        alert("Fallo la conexión. Revisa la consola para más detalles.");
    }
}



// DESIGN
// ── Demo stub: replace this function body with your real algorithm logic ──
function runAnalysis() {
    const capacity = parseFloat(document.getElementById('maxCapacity').value);
    if (!capacity || capacity <= 0) {
      alert('Please enter a valid container capacity (kg).');
      return;
    }

    // Placeholder result display — wire up your real algorithm here
    const dpVal   = Math.round(capacity * 8.6);
    const dpWt    = Math.round(capacity * 0.93);
    const grVal   = Math.round(capacity * 8.1);
    const grWt    = Math.round(capacity * 0.89);

    document.getElementById('dp-value').textContent  = '$' + dpVal.toLocaleString();
    document.getElementById('dp-weight').textContent = dpWt + ' kg';
    document.getElementById('dp-packages').innerHTML =
      ['Pkg A – 120 kg', 'Pkg C – 85 kg', 'Pkg D – 210 kg']
        .map(p => `<div style="background:rgba(62,95,68,0.2);border-radius:8px;padding:6px 12px;margin-bottom:6px;font-size:13px;color:#9EC9A5;font-style:normal;">📦 ${p}</div>`)
        .join('');

    document.getElementById('greedy-value').textContent  = '$' + grVal.toLocaleString();
    document.getElementById('greedy-weight').textContent = grWt + ' kg';
    document.getElementById('greedy-packages').innerHTML =
      ['Pkg A – 120 kg', 'Pkg D – 210 kg']
        .map(p => `<div style="background:rgba(94,123,99,0.2);border-radius:8px;padding:6px 12px;margin-bottom:6px;font-size:13px;color:#9EC9A5;font-style:normal;">📦 ${p}</div>`)
        .join('');
  }


  // Inicializar Lenis
const lenis = new Lenis({
    duration: 1.5,    
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), 
    smoothWheel: true,
    touchMultiplier: 2,
});

function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
}

requestAnimationFrame(raf);

// scroll navbar
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault(); 
        
        const target = document.querySelector(this.getAttribute('href'));
        
        if (target) {
            lenis.scrollTo(target, {
                duration: 1.5, 
                offset: -50    
            });
        }
    });
});