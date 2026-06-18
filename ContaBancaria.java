package br.com.etechas.models;

public abstract class ContaBancaria {

    protected String numero;
    protected double saldo;

    public void exibirSaldo() {
        System.out.println("Saldo: " + saldo);
    }
}
