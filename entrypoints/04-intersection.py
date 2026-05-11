import numpy as np
import urenderer

# Renderize uma cena em que o algoritmo de oclusão falha
#
# Observe o método urenderer.renderer.pyplot_renderer.PyplotRenderer::end
# Ele desenha a cena utilizando o "algoritmo do pintor" (painter's algorithm)
# para determinar a visibilidade dos triângulos (qual deve estar por cima do outro)
#
# Crie uma cena com dois cubos de forma que o algoritmo do pintor falhe de forma
# visualmente perceptível.

if __name__ == "__main__":
    urenderer.utils.clear_workdir("04-intersection")
    renderer = urenderer.renderer.PyplotRenderer(1920, 1080)
    runtime = urenderer.application.Runtime(renderer, name="04-intersection")

    cube0 = urenderer.node.Node()
    cube1 = urenderer.node.Node()

    cube0.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    cube1.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()

    # Dois cubos em profundidades proximas
    cube0.translation = np.array([-0.3, 0.0, -5.0], dtype=np.float64)
    cube1.translation = np.array([ 0.3, 0.0, -5.0], dtype=np.float64)

    # Rotações diferentes para que eles se atravessem visualmente
    cube0.rotation = np.array([0.0, 45.0, 0.0], dtype=np.float64)
    cube1.rotation = np.array([45.0, 0.0, 0.0], dtype=np.float64)

    cube0.scale = np.array([1.5, 1.5, 1.5], dtype=np.float64)
    cube1.scale = np.array([1.5, 1.5, 1.5], dtype=np.float64)

    runtime.scene.add_child(cube0)
    runtime.scene.add_child(cube1)

    runtime.iter(capture=True)