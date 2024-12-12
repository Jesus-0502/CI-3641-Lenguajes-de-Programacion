// CI-3641 Lenguajes de Programación
// Alumno: Jesus Gutierrez
// Carnet: 20-10332
// Pregunta 1. Inciso 3

struct conjuntoPersonas {

    struct Persona: Hashable {
        let nombre: String
        let edad: Int
    }
    private var personas: Set<Persona> = []

    func cantidadPersonas() -> Int {
        return personas.count
    }

    func mayoresEdad() -> Set<Persona> {
        var mayoresEdad: Set<Persona> = []

        for persona in personas {
            if persona.edad >= 18 {
                mayoresEdad.insert(persona)
            }   
        }

        return mayoresEdad
    }

    func nombreComun() -> String {
        var dict: [String: Int] = [:]

        for persona in personas{

            if let contador = dict[persona.nombre] {
                 dict[persona.nombre] = contador + 1
            } 
            else {
                dict[persona.nombre] = 1
            }
        }

        var nombreMasComun = ""
        var maxContador = 0

        for (key, value) in dict {
            if value > maxContador {
                maxContador = value
                nombreMasComun = key
            }
        }

        return nombreMasComun
    }

}

