import numpy as np
import urenderer

# Crie uma cena contendo uma pirâmide e renderize ela
#
# Implemente urenderer.geometry.polygonal_ifs.get_ifs_pyramid para obter a geometria de uma pirâmide

if __name__ == "__main__":
    urenderer.utils.clear_workdir("02-pyramid")
    renderer = urenderer.renderer.PyplotRenderer(1920, 1080)
    runtime = urenderer.application.Runtime(renderer, name="02-pyramid")

    pyramid = urenderer.node.Node()

    pyramid.translation = np.array([0, 0, -5], np.float64)
    pyramid.rotation = np.array([45, 45, 45], np.float64)
    pyramid.render_data = urenderer.geometry.polygonal_ifs.get_ifs_pyramid()

    runtime.scene.add_child(pyramid)

    runtime.iter(capture=True)