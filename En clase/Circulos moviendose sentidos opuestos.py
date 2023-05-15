from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.Uniform import Uniform
from OpenGL.GL import *
from math import sin, cos , pi
### Autor: Mauricio González Torres
class Test(Base):
    def initialize(self):
        print("Initializing program...")

        ### initialize program ###
        vsCode = """
        in vec3 position;
        uniform vec3 translation;
        uniform float scale;
        void main()
        {
            vec3 pos = position + translation;
            pos *= scale;
            gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
        }
        """
        fsCode = """
        uniform vec3 baseColor;
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        ### render settings (optional) ###
        # specify color used when clearing
        glClearColor(0.0, 0.0, 0.0, 1.0)

        ### set up vertex array object ###
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        ### Establece vertices de atributo para el circulo 1  ###
        
        positionData = [] # vertex para la formación del circulo
        for i in range(360):
            theta = i * pi/ 180.0
            x = cos(theta)
            y = sin(theta)
            positionData.append([x, y, 0.0])
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

        ### Establece las variables uniformes para el primer círculo ###
        self.redTranslation = Uniform("vec3", [-0.5, 0.0, 0.0])
        self.redTranslation.locateVariable(self.programRef, "translation")
        self.scale = Uniform("float", 0.5)  # valor de escalado inicial
        self.scale.locateVariable(self.programRef, "scale")
        self.baseColor = Uniform("vec3", [1.0, 0.0, 0.0])
        self.baseColor.locateVariable(self.programRef, "baseColor")

        ### Establece vertices de atributo para el circulo 2 ###
        positionData2 = []
        for i in range(360):
            theta = i * pi/ 180.0
            x = cos(theta) * 0.5  # Escala para hacerlo más pequeño
            y = sin(theta) * 0.5
            positionData2.append([x, y, 0.0])
        positionAttribute2 = Attribute("vec3", positionData2)
        positionAttribute2.associateVariable(self.programRef, "position")

        ### Establece las variables uniformes para el segundo círculo ###
        self.blueTranslation = Uniform("vec3", [0.5, 0.0, 0.0])  # posicion inicial
        self.blueTranslation.locateVariable(self.programRef, "translation")
        self.scaleBlue = Uniform("float", 0.5)  # Escala inicial
        self.scaleBlue.locateVariable(self.programRef, "scale")
        self.baseColor2 = Uniform("vec3", [0.0, 0.0, 1.0])  # color azul
        self.baseColor2.locateVariable(self.programRef, "baseColor")

    def update(self):         
        ### Actualiza información  del circulo rojo ###
        self.redTranslation.data[0] = -0.75 * cos(self.time)
        self.redTranslation.data[1] = 0.75 * sin(self.time)
        self.scale.data = 0.25

        ### update data for blue circle ###
        self.blueTranslation.data[0] = 0.75 * cos(self.time)
        self.blueTranslation.data[1] = 0.75 * sin(self.time)  
        self.scaleBlue.data = 0.25

        ### render scene ###
        # reset color buffer with specified color
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(self.programRef)

        # render círculo rojo
        self.redTranslation.uploadData()
        self.scale.uploadData()
        self.baseColor.uploadData()
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)

        # render círculo azul
        self.blueTranslation.uploadData()
        self.scaleBlue.uploadData()
        self.baseColor2.uploadData()
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)

Test().run()