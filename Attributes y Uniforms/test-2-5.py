from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *

# render two triangles with vertex colors
class Test(Base):

    # initialize(self): Este método inicializa el programa y los atributos de los
    # vértices. En primer lugar, se crea el código del shader de vértices y del shader
    # de fragmentos. Luego, se utiliza la función OpenGLUtils.initializeProgram para 
    # inicializar el programa y obtener su referencia. A continuación, se configuran
    #  los valores de renderizado para los puntos y las líneas. Luego, se crea el 
    # objeto de array de vértices y se asocian los atributos de posición y color a
    #  las variables de shader correspondientes.
    def initialize(self):
        print("Initializing program...")
        ### initialize program ###
        vsCode = """
            in vec3 position;
            in vec3 vertexColor;
            out vec3 color;
            void main()
            {
                gl_Position = vec4(position.x, position.y, position.z, 1.0);
                color = vertexColor;
            }
        """
        fsCode = """
            in vec3 color;
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(color.r, color.g, color.b, 1.0);
            }
        """
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        ### render settings (optional) ###
        glPointSize(10)
        glLineWidth(4)

        ### set up vertex array object ###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        ### set up vertex attributes ###
        positionData = [
            [0.0, 0.0, 0.0],
            [0.5, 0.5, 0.0],
            [0.5, -0.5, 0.0],
            [-0.5, -0.5, 0.0],
            [-0.5, 0.5, 0.0],
            [0.0, 0.0, 0.0]
        ]
        self.vertexCount = len(positionData)

        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

        colorData = [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ]
        colorAttribute = Attribute("vec3", colorData)
        colorAttribute.associateVariable(self.programRef, "vertexColor")

    #update(self): Este método se encarga de renderizar la escena. Se utiliza la función glUseProgram para indicar el programa que se utilizará
    def update(self):
        glUseProgram(self.programRef)
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

# instantiate this class and run the program
Test().run()
