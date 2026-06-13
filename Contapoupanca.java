package br.com.etechas.models;


import br.com.etechas.Interface.IOperavel;

public class Contapoupanca extends ContaBancaria implements IOperavel {

    public void depositar(double valor){
        saldo += valor;
    }
public void sacar(double valor) {
    saldo -= valor;
    }
}
