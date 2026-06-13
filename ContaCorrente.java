package br.com.etechas.models;
import br.com.etechas.Interface.IOperavel;


public class ContaCorrente extends ContaBancaria implements IOperavel {

    private double taxaSaque;

    public void depositar(double valor){
        saldo += valor;
    }
    public void sacar(double valor){
        saldo -= valor;
    }

}
