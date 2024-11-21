indirect enum Church {
    case Cero
    case Suc(Church)

    func valor() -> Int {
        switch self {
        case .Cero:
            return 0
        case .Suc(let n):
            return 1 + n.valor()
        }
    }

    func suma(_ n: Church) -> Church {
        switch self {
            case .Cero:
                return n
            
            case .Suc(let m):
                return .Suc(m.suma(n))
        }
    }

    func multiplicacion(_ n: Church) -> Church {
        switch self {
            case .Cero:
                return .Cero
            case .Suc(let m):
                return n.suma(m.multiplicacion(n))
        }
    }
}
