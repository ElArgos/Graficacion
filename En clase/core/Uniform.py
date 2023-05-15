from OpenGL.GL import *
import numpy

class Uniform(object):
    #__init__(self, dataType): el constructor de la clase, que recibe como parámetro
    #  el tipo de dato de la variable uniforme.
    def __init__(self, dataType, data):
        # type of data:
        # int | bool | float | vec2 | vec3 | vec4
        self.dataType = dataType
        # data to be sent to uniform variable
        self.data = data
        # reference for variable location in program
        self.variableRef = None

    # get and store reference for program variable with given name
    # obtiene la ubicación de la variable uniforme en el programa de shaders
    def locateVariable(self, programRef, variableName):
        self.variableRef = glGetUniformLocation(programRef, variableName)
        #getLocation(self, programRef): un método que obtiene la ubicación de la variable uniforme en el programa de shaders.
    # store data in uniform variable previously located
    # uploadData almacena los datos en la variable uniforme previamente ubicada.
    def uploadData(self):
        # if the program does not reference the variable, then exit
        if self.variableRef == -1:
            return
        if self.dataType == "int":
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == "bool":
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == "float":
            glUniform1f(self.variableRef, self.data)
        elif self.dataType == "vec2":
            glUniform2f(self.variableRef, self.data[0], self.data[1])
        elif self.dataType == "vec3":
            glUniform3f(self.variableRef, self.data[0], self.data[1],self.data[2])
        elif self.dataType == "vec4":
            glUniform4f(self.variableRef, self. data[0], self.data[1], self.data[2], self.data[3])