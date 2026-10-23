import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime

# ---------------------------------------------------------
# 1. Configuración de la página y Estilos CSS
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ecosistema de Erradicación del Trabajo Infantil RD",
    page_icon="🇩🇴",
    layout="wide"
)

# Estilos personalizados para la tipografía y contenedores
st.markdown("""
    <style>
    .main-title {
        font-size: 26px;
        font-weight: 800;
        color: #1E3A8A;
        text-align: center;
        margin-top: 10px;
    }
    .sub-title {
        font-size: 15px;
        color: #059669;
        text-align: center;
        font-weight: 600;
        margin-bottom: 20px;
    }
    .consortium-box {
        background-color: #F8FAFC;
        padding: 12px;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. Encabezado e Integración de Logos Institucionales
# ---------------------------------------------------------
st.markdown('<div class="main-title">Transformación Sistémica: Erradicación del Trabajo Infantil en Vertederos</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Un modelo intersectorial para la transición hacia una economía circular inclusiva en RD</div>', unsafe_allow_html=True)

st.markdown('<div class="consortium-box">', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold; color: #334155; margin-bottom: 10px;'>🏛️ Consorcio Intersectorial Aliado</p>", unsafe_allow_html=True)

col_logo1, col_logo2, col_logo3, col_logo4, col_logo5, col_logo6 = st.columns(6)

with col_logo1:
    try:
        st.image("Banco BHD.png", width=85)
    except:
        st.markdown("**Banco BHD**")
    st.caption("Capital & Bancarización")

with col_logo2:
    try:
        st.image("superintendencia de bancos.png", width=85)
    except:
        st.markdown("**Sup. de Bancos**")
    st.caption("Regulación & Cumplimiento")

with col_logo3:
    try:
        st.image("DO Sostenible.png", width=85)
    except:
        st.markdown("**DO Sostenible**")
    st.caption("Infraestructura y Cierre")

with col_logo4:
    try:
        st.image("Fundacion Katherin Batista.jpg", width=85)
    except:
        st.markdown("**Fundación K. Batista**")
    st.caption("Territorio & Confianza")

with col_logo5:
    try:
        st.image("Tikunia Group .png", width=85)
    except:
        st.markdown("**Tikunia Group**")
    st.caption("Datos & Trazabilidad")

with col_logo6:
    try:
        st.image("Barna Management School.png", width=85)
    except:
        st.markdown("**Barna Management**")
    st.caption("Sostenibilidad e Impacto")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. Base de Datos / Estado de Sesión con Enfoque de Tríada
# ---------------------------------------------------------
if "reportes" not in st.session_state:
    st.session_state.reportes = pd.DataFrame([
        {
            "id": "REP-001",
            "fecha": "2026-10-20 10:30",
            "provincia": "Santo Domingo",
            "vertedero": "Vertedero de Duquesa (Zona Cero)",
            "menores": 50,
            "riesgo": "Crítico",
            "iniciativa": "Iniciativa 1: Retiro y Nivelación Escolar (Fundación Batista)",
            "estado": "En Censo / Salvaguarda",
            "latitud": 18.5714,
            "longitud": -69.9328
        },
        {
            "id": "REP-002",
            "fecha": "2026-10-21 14:15",
            "provincia": "Santiago",
            "vertedero": "EcoParque Rafey",
            "menores": 15,
            "riesgo": "Alto",
            "iniciativa": "Iniciativa 2: Bono de Transición Familiar (Banco BHD)",
            "estado": "Bancarización / Inclusión",
            "latitud": 19.4678,
            "longitud": -70.7301
        },
        {
            "id": "REP-003",
            "fecha": "2026-10-22 09:00",
            "provincia": "Peravia",
            "vertedero": "Vertedero Municipal Baní",
            "menores": 8,
            "riesgo": "Medio",
            "iniciativa": "Iniciativa 3: Cadena de Valor Trazable (Tikunia / DO Sostenible)",
            "estado": "Auditoría / Acopio Seguro",
            "latitud": 18.2792,
            "longitud": -70.3319
        }
    ])

# ---------------------------------------------------------
# 4. Disposición Principal: Tabs de Navegación UX
# ---------------------------------------------------------
tab_mapa, tab_nuevo_reporte, tab_metricas = st.tabs([
    "🗺️ Mapa & Seguimiento Nacional", 
    "🚨 Registrar Alerta / Incidencia", 
    "📈 Métricas de Impacto (GRI 3)"
])

# =========================================================
# TAB 1: Mapa Interactivo y Visualización por Inconveniente
# =========================================================
with tab_mapa:
    col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
    
    total_reportes = len(st.session_state.reportes)
    total_menores = st.session_state.reportes["menores"].sum()
    casos_criticos = len(st.session_state.reportes[st.session_state.reportes["riesgo"] == "Crítico"])
    
    col_kpi1.metric("Total Incidentes", total_reportes)
    col_kpi2.metric("Menores Identificados", total_menores)
    col_kpi3.metric("Focos Críticos (Duquesa/Otros)", casos_criticos)
    col_kpi4.metric("Niv. Retención Escolar", "85% Target", delta="Meta GRI")

    st.markdown("---")
    
    # Mapa Folium
    mapa_rd = folium.Map(location=[18.7357, -70.1627], zoom_start=8, tiles="OpenStreetMap")
    
    colores_riesgo = {"Crítico": "red", "Alto": "orange", "Medio": "yellow", "Bajo": "green"}
    
    for idx, row in st.session_state.reportes.iterrows():
        popup_html = f"""
        <div style="font-family: Arial; width: 220px;">
            <h4 style="margin-bottom:5px;"><b>{row['id']}</b></h4>
            <p style="margin:2px 0;"><b>Lugar:</b> {row['vertedero']}</p>
            <p style="margin:2px 0;"><b>Menores:</b> {row['menores']}</p>
            <p style="margin:2px 0;"><b>Iniciativa Asignada:</b><br><small>{row['iniciativa']}</small></p>
            <p style="margin:2px 0;"><b>Estado:</b> {row['estado']}</p>
        </div>
        """
        folium.Marker(
            location=[row["latitud"], row["longitud"]],
            popup=folium.Popup(popup_html, max_width=250),
            tooltip=f"{row['id']} - {row['vertedero']}",
            icon=folium.Icon(color=colores_riesgo.get(row["riesgo"], "blue"), icon="info-sign")
        ).add_to(mapa_rd)
        
    st_folium(mapa_rd, width="100%", height=450)
    
    st.subheader("📋 Matriz de Trazabilidad e Intervención")
    st.dataframe(
        st.session_state.reportes[["id", "fecha", "provincia", "vertedero", "menores", "riesgo", "iniciativa", "estado"]],
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# TAB 2: Formulario Optimizado UX según la Tríada
# =========================================================
with tab_nuevo_reporte:
    st.subheader("📝 Formulario de Registro Intersectorial")
    st.info("💡 La información registrada se deriva automáticamente al pilar correspondiente (Social, Económico o Mercado) según el Consorcio Interinstitucional.")
    
    with st.form("form_triada", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            provincia = st.selectbox("Provincia / Región:", ["Santo Domingo (Duquesa)", "Santiago (Rafey)", "Peravia (Baní)", "La Vega", "San Cristóbal", "Otra"])
            vertedero = st.text_input("Nombre del Vertedero / Sector de Acopio:", placeholder="Ej. Vertedero de Duquesa")
            menores = st.number_input("Cantidad aproximada de menores detectados:", min_value=1, max_value=100, value=1)
        
        with c2:
            riesgo = st.selectbox("Nivel de Riesgo Observado:", ["Crítico", "Alto", "Medio", "Bajo"])
            iniciativa_prioritaria = st.selectbox(
                "Canalizar Intervención Hacia:",
                [
                    "Iniciativa 1: Retiro y Nivelación Escolar (Fundación K. Batista)",
                    "Iniciativa 2: Bono de Transición y Medios de Vida (Banco BHD)",
                    "Iniciativa 3: Trazabilidad y Cero Trabajo Infantil (DO Sostenible / Tikunia)"
                ]
            )
            lat = st.number_input("Latitud:", value=18.5714, format="%.4f")
            lng = st.number_input("Longitud:", value=-69.9328, format="%.4f")

        observaciones = st.text_area("Detalles de la Situación y Entorno Familiar:", placeholder="Describa la actividad económica informal, presencia de adultos, o necesidades inmediatas de apoyo escolar/nutricional...")
        
        submitted = st.form_submit_button("🚨 Enviar Reporte al Ecosistema", use_container_width=True)
        
        if submitted:
            nuevo_id = f"REP-00{len(st.session_state.reportes) + 1}"
            nueva_fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
            
            nuevo_reporte = {
                "id": nuevo_id,
                "fecha": nueva_fecha,
                "provincia": provincia,
                "vertedero": vertedero if vertedero else "Zona no especificada",
                "menores": menores,
                "riesgo": riesgo,
                "iniciativa": iniciativa_prioritaria,
                "estado": "Notificado a Red de Apoyo",
                "latitud": lat,
                "longitud": lng
            }
            
            st.session_state.reportes = pd.concat([st.session_state.reportes, pd.DataFrame([nuevo_reporte])], ignore_index=True)
            st.success(f"✅ ¡Incidencia **{nuevo_id}** canalizada exitosamente!")

# =========================================================
# TAB 3: Dashboard de Métricas e Impacto (Sostenibilidad)
# =========================================================
with tab_metricas:
    st.subheader("🎯 Monitoreo de Impacto por Pilar (GRI 3 & ODS)")
    
    col_m1, col_m2, col_m3 = st.columns(3)
    
    with col_m1:
        st.markdown("### 📘 Pilar Social")
        st.markdown("**Ejecutado por Fundación K. Batista**")
        st.progress(0.85)
        st.caption("85% Retención Escolar y Apoyo Nutricional alcanzado en programa piloto (ODS 3, 4).")
        
    with col_m2:
        st.markdown("### 💳 Pilar Económico")
        st.markdown("**Liderado por Banco BHD**")
        st.progress(0.65)
        st.caption("Índice de bancarización y entregas de Bonos de Transición Condicionados (ODS 1, 8).")
        
    with col_m3:
        st.markdown("### ♻️ Pilar Mercado & Trazabilidad")
        st.markdown("**Tikunia Group & DO Sostenible**")
        st.progress(0.40)
        st.caption("Toneladas de residuos reciclados bajo certificación libre de trabajo infantil (ODS 10, 17).")