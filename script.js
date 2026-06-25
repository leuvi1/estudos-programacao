function verificarFraude(valorCompra, localSuspeito) {
    if (valorCompra > 2000 && localSuspeito == true) {
        return "BLOQUEADO: Transação de alto valor em local suspeito.";
    } else if (valorCompra > 2000 && localSuspeito == false) {
        return "ALERTA: Compra de alto valor detectada. Notificar cliente.";
    } else {
        return "APROVADO: Transação liberada com sucesso.";
    }
}
console.log(verificarFraude(3500, true));
console.log(verificarFraude(2500, false));
console.log(verificarFraude(450, false));
