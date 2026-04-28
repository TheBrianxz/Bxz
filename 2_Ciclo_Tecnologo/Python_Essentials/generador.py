cat << 'EOF' > generador.py
from weasyprint import HTML
import os

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <style>
        @page { size: A4; margin: 25mm 20mm; }
        body { font-family: sans-serif; color: #333; line-height: 1.6; }
        .date { text-align: right; }
        h2 { color: #1a5f7a; border-left: 5px solid #1a5f7a; padding-left: 10px; }
        .section-title { font-weight: bold; color: #1a5f7a; }
        .content { text-align: justify; }
        .signature { margin-top: 50px; }
    </style>
</head>
<body>
    <div class="date">Bogotá D.C., 20 de abril de 2026</div>
    <div class="recipient">
        <strong>Para:</strong> Diego Fernando Reyes Franco<br>
        <strong>De:</strong> Brian Edilxon Alvernia Rodriguez<br>
        Estudiante de Ingeniería de Sistemas
    </div>
    <div class="subject"><strong>Asunto: Definición de la problemática del proceso investigativo</strong></div>
    <div class="content">
        <p>Estimado Docente, presento la definición de la problemática seleccionada:</p>
        <h2>Problemática: Sobrecarga Sensorial y Cognitiva en Usuarios Neurodivergentes</h2>
        <p><span class="section-title">1. Ingeniería de Sistemas:</span> Arquitecturas con procesos intrusivos y falta de protocolos de filtrado de ruido técnico.</p>
        <p><span class="section-title">2. Comunicación Visual:</span> Interfaces saturadas y falta de jerarquía visual que genera fatiga cognitiva.</p>
        <p><span class="section-title">3. Usuario Final:</span> Personas neurodivergentes que sufren exclusión por entornos digitales hostiles.</p>
        <p><strong>Solución:</strong> Modelo de "Interfaz Calma" (Calm UI).</p>
    </div>
    <div class="signature">Atentamente,<br><br><strong>Brian Edilxon Alvernia Rodriguez</strong></div>
</body>
</html>
"""
output_filename = "definicion-problematica-brian-alvernia.pdf"
HTML(string=html_content).write_pdf(output_filename)
