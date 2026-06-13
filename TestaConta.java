package br.com.etechas;

import br.com.etechas.models.*;

public class TestaConta {

    public static void main(String[] args) {

        ContaCorrente cc = new ContaCorrente();

        cc.depositar(1000);
        cc.sacar(200);

        cc.exibirSaldo();

    }
}