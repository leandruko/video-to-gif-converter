import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile
import os

# Función para convertir el video a GIF
def convert_to_gif(video_path, gif_path, fps):
    clip = VideoFileClip(video_path)
    clip.write_gif(gif_path, fps=fps)

# Título de la aplicación
st.title("Video converter to GIF")

# Subir archivo de video
uploaded_file = st.file_uploader("Sube tu video", type=["mp4", "avi", "mov"])

# Campo para ajustar los FPS
fps = st.slider("Ajusta los FPS para el GIF", min_value=1, max_value=60, value=10)

# Convertir el video si se ha subido
if uploaded_file:
    # Crear un archivo temporal para almacenar el video
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        video_path = tmp_file.name

    st.video(uploaded_file)  # Mostrar el video subido

    # Convertir el video a GIF cuando se hace clic en el botón
    if st.button("Convertir a GIF"):
        with st.spinner("Convirtiendo el video a GIF..."):
            # Crear un archivo temporal para el GIF
            gif_path = os.path.join(tempfile.gettempdir(), "output.gif")
            convert_to_gif(video_path, gif_path, fps)
            
            # Mostrar el GIF generado
            st.success("¡Conversión completada!")
            st.image(gif_path)

            # Botón para descargar el GIF
            with open(gif_path, "rb") as f:
                gif_bytes = f.read()
                st.download_button(
                    label="Descargar GIF",
                    data=gif_bytes,
                    file_name="output_gif.gif",
                    mime="image/gif"
                )
