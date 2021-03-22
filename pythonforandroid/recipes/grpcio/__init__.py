from pythonforandroid.recipe import PythonRecipe
class GrpcioRecipe(PythonRecipe):
    version = 'master'
    url = 'https://github.com/grpc/grpc/archive/{version}.zip'
    name = 'grpcio'

    depends = ['six', 'futures', 'enum34']

recipe = GrpcioRecipe()