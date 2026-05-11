import numpy as np
import urenderer

# Crie uma cena com três objetos, um filho do outro:
# Objeto0 -> Objeto1 -> Objeto2
#
# Configure as transformações para que todos os objetos sejam visíveis e renderize a cena
#
# Altere a transformação do objeto avô dos outros e renderize a cena.
# Observe como que os objetos filhos se movem juntos

if __name__ == "__main__":
    urenderer.utils.clear_workdir("03-grandchild")
    renderer = urenderer.renderer.PyplotRenderer(1920, 1080)
    runtime = urenderer.application.Runtime(renderer, name="03-grandchild")

    objeto0 = urenderer.node.Node()
    objeto1 = urenderer.node.Node()
    objeto2 = urenderer.node.Node()

    objeto0.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    objeto1.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    objeto2.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()

    # O nó avô fica mais afastado da câmera
    objeto0.translation = np.array([0, 0, -6], dtype=np.float64)

    # O filho é deslocado em relação ao pai
    objeto1.translation = np.array([1.5, 0, 0], dtype=np.float64)

    # O neto é deslocado em relação ao filho
    objeto2.translation = np.array([1.5, 0, 0], dtype=np.float64)

    #objeto0.scale = np.array([0.5, 0.5, 0.5], dtype=np.float64)
    #objeto1.scale = np.array([0.5, 0.5, 0.5], dtype=np.float64)
    #objeto2.scale = np.array([0.5, 0.5, 0.5], dtype=np.float64)

    objeto0.add_child(objeto1)
    objeto1.add_child(objeto2)

    runtime.scene.add_child(objeto0)

    runtime.iter(capture=True)

    # Rotacione o nó avô
    objeto0.rotation = np.array([0, 45, 0], dtype=np.float64)

    runtime.iter(capture=True)