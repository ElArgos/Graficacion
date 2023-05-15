from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.Uniform import Uniform
from OpenGL.GL import *
from math import sin, cos , pi


# animate circle moving across screen
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

        ### set up vertex attribute ###
        # vertex positions for a circle
        positionData = []
        for i in range(360):
            theta = i * pi/ 180.0
            x = cos(theta)
            y = sin(theta)
            positionData.append([x, y, 0.0])
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

        ### set up uniforms ###
        self.translation = Uniform("vec3", [-0.5, 0.0, 0.0])
        self.translation.locateVariable(self.programRef, "translation")
        self.scale = Uniform("float", 0.5)  # initial scale value
        self.scale.locateVariable(self.programRef, "scale")
        self.baseColor = Uniform("vec3", [1.0, 0.0, 0.0])
        self.baseColor.locateVariable(self.programRef, "baseColor")

    def update(self):
        ### update data ###
        self.translation.data[0] = 0.75 * cos(self.time)
        self.translation.data[1] = 0.75 * sin(self.time)
        self.scale.data = 0.25  # new scale value
        ### render scene ###
        # reset color buffer with specified color
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(self.programRef)
        self.translation.uploadData()
        self.scale.uploadData()
        self.baseColor.uploadData()
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)

# instantiate this class and run the program
Test().run()
