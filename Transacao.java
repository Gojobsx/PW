package br.com.etechas.models;

import br.com.etechas.Interface.IOperavel;

public class Transacao {

    public void aplicar(IOperavel op, double valor, boolean deposito) {

        if (deposito) {
            op.depositar(valor);
        } else {
            op.sacar(valor);
        }

    }
}