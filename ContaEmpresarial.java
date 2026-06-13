package br.com.etechas.models;

import br.com.etechas.Interface.IOperavel;

public class ContaEmpresarial extends ContaBancaria implements IOperavel {

    private double limitecredito;

    public void depositar(double valor){
        saldo += valor;
    }
    public void sacar(double valor){
        saldo -= valor;
    }
}
