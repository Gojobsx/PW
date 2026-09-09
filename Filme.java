package br.com.etechas.ingressos.entity;

import br.com.etechas.ingressos.enums.ClassificacaoIndicativaEnum;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@Entity
@Table(name="TBL_FILME")
public class Filme {
    @Id //PRIMARY KEY
    @Column(name="ID_FILME")
    @GeneratedValue(strategy = GenerationType.IDENTITY) //Identity
    private long id;
    @Column(name = "TX_NOME")
    private String nome;
    @Column(name = "NR_DURACAO")
    private Integer duracao;
    @Column(name = "TP_CATEGORIA")
    @Enumerated(EnumType.STRING)
    private br.com.etechoracio.ingresso.enums.CategoriaFilmeEnum categoria;
    @Column(name = "TP_CLASSIFICACAO")
    private ClassificacaoIndicativaEnum classificacao;
    @Column(name = "NR_ANO")
    private Integer ano;
    @Column(name = "TX_CAPA")
    private String capa;
    @Column(name = "TX_DIRETOR")
    private String diretor;
    @Column(name = "TX_ELENCO")
    private String elenco;
    @Column(name = "TX_DESCRICAO")
    private String descricao;
    @Column(name = "NR_AVALIACAO")
    private double avaliacao;
    @Enumerated(EnumType.STRING)
    @Column(name = "CHK_EM_CARTAZ")
    private br.com.etechoracio.ingresso.enums.SimNaoEnum emCartaz;

    public Filme(long id, String nome, ClassificacaoIndicativaEnum ClassificacaoIndicativaEnum, br.com.etechoracio.ingresso.enums.SimNaoEnum simNaoEnum) {
        this.id = id;
        this.nome = nome;
        this.classificacao = ClassificacaoIndicativaEnum;
        this.emCartaz = simNaoEnum;
    }
}
