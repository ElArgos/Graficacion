from core.base import Base 
from core.openGLUtils import OpenGLUtils 
from core.attribute import Attribute 
from OpenGL.GL import *

# Renderiza una corona
class Test(Base):
    # El método initialize() es llamado una sola vez en el inicio del programa
    #  y se encarga de inicializar el programa OpenGL y configurar el renderizado.
    #  Primero se inicializa el programa definiendo los shaders de vértices y
    #  fragmentos. En este caso, solo se define el shader de vértices que se encarga
    #  de transformar la posición de los vértices en pantalla.
    def initialize(self):
        print("Initializing program...")

        ### initialize program ###
        vsCode = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """
        fsCode = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        ### render settings (optional) ###
        #se configuran los parámetros de renderizado opcionales. En este caso, se establece el grosor de la línea a 4 unidades.
        glLineWidth(4)

        ### set up vertex array object
        # Se crea un Vertex Array Object (VAO) que permite encapsular
        #  y organizar los atributos de los vértices. Se activa el VAO y se crea 
        # un atributo de posición para los vértices que se van a renderizar.
       
        vaoRef = glGenVertexArrays(1) 
        glBindVertexArray(vaoRef)

        ### set up vertex attribute ###
         # En este caso, se definen seis vértices en forma de corona.
         #  Se guarda la cantidad de vértices en la variable vertexCount.
        positionData = [[0.8, 0.8, 0.0], [0.8, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.8, 0.0], [0.0, 0.0, 0.0], [0.8, 0.0, 0.0]]
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

    def update(self):
        glUseProgram(self.programRef)
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

# instantiate this class and run the program 
Test().run()
