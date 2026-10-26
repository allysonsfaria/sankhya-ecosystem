---
id: "1500003568962"
titulo: "Auditoria de Modificações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003568962-Auditoria-de-Modifica%C3%A7%C3%B5es"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-24T14:22:53Z"
rotulos: ["Produtos", "Configuração", "Segurança", "Parceiro", "auditoria de modificações", "br.com.sankhya.mge.RegistroModificacoes", "Auditoria de Modificações no Sankhya", "Detalhamento das modificações", "Controle de Acesso", "Auditoria"]
---

# Auditoria de Modificações

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42310464258455)Módulo: Configurações>Controle de Acesso ![Versão](https://ajuda.sankhya.com.br/hc/article_attachments/42310434566423)Versão disponível: A partir da 4.6
```

---

Através dessa tela é possível auditar tabelas e seus campos do sistema, mostrando quem fez uma determinada alteração na data/hora em que foi realizada.

Essa rotina é dividida em três partes, sendo elas:

[Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003568962-Auditoria-de-Modifica%C3%A7%C3%B5es#filtros)                                                                                  [Informações gerais das modificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003568962-Auditoria-de-Modifica%C3%A7%C3%B5es#informa%C3%A7%C3%B5esgeraisdasmodifica%C3%A7%C3%B5es)

[Detalhamento das modificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003568962-Auditoria-de-Modifica%C3%A7%C3%B5es#detalhamentodasmodifica%C3%A7%C3%B5es)

![Imagem 3: Detalhamento das modificações](https://ajuda.sankhya.com.br/hc/article_attachments/4418213367319)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003568962-Auditoria-de-Modifica%C3%A7%C3%B5es#top)

### Filtros

No Painel de Filtros, que está destacado na imagem abaixo, é possível que você pesquise pelo nome da **"Tabela"** ou da **"Instância"**, pelo nome do **"Campo"**, valor da **"Chave"** modificada, pelo **"Período"** (data inicial e data final), pelo nome ou código do **"Usuário"** que realizou a modificação ou ainda, pelo **"Tipo de Alteração"** feita, que pode ser de **"Edição"**, **"Remoção"** ou **"Inserção"**.

![Imagem 4: No Painel de Filtros , que está destacado na imagem abaixo, é possível que você pesquise pelo nome da "Tabela" ou da…](https://ajuda.sankhya.com.br/hc/article_attachments/4418213393047)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003568962-Auditoria-de-Modifica%C3%A7%C3%B5es#top)

### Informações gerais das modificações

Nessa grade serão exibidas as alterações realizadas nas tabelas previamente mapeadas como, por exemplo, o nome da Instância e o nome da Tabela, Data/hora, a Chave, o Tipo e o nome/código do Usuário Responsável.

![Imagem 5: Nessa grade serão exibidas as alterações realizadas nas tabelas previamente mapeadas como, por exemplo, o nome da…](https://ajuda.sankhya.com.br/hc/article_attachments/4418213435159)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003568962-Auditoria-de-Modifica%C3%A7%C3%B5es#top)

### Detalhamento das modificações

Por fim, quando você clicar em uma linha de alteração no guia geral de informações, essa grade será alterada, exibindo os campos que foram modificados, com o **"Nome do Campo"**, o **"Valor antes"** e o **"Valor depois"**.

![Imagem 6: Por fim, quando você clicar em uma linha de alteração no guia geral de informações, essa grade será alterada, exibindo…](https://ajuda.sankhya.com.br/hc/article_attachments/4418206285335)

**Observação:** caso o Valor antes esteja vazio, significa que foi um Tipo de Alteração de Inserção.

**Importante:** as tabelas abaixo são as que serão auditadas permanentemente pelo sistema e que sairão previamente configuradas:

- **TSIPAR -** Parâmetros
- **TGFPAR -** Parceiros
- **TGFPRO -** Produtos
- **TGFTPV -** Tipos de Negociação
- **TGFTOP -** Tipos de Operação
- **TGFEMP -** EmpresaFinanceiro
- **TSIEMP -** Empresas
- **TGFPPG -** Gestão Fiscal Parcelas de Pagamento
- **TGFCTB -** Parâmetros Contabilização
- **TSICTA -** Contas Bancárias (ignorar as alterações nas colunas: REMBCO, SALDOBCO, SALDOREAL, SEQREM e SEQREM2)
- **TCBEMP -** Empresas (contabilidade)
- **TFPEMP -** Empresa Pessoal
- **TFPFUN -** Funcionários
- **TFPEVE -** Eventos
- **TFPFOR -** FP Fórmulas de Cálculo
- **TGFMODTOP -** Modelos da TOP
- **TGFFOR -** Fórmulas de Precificação
- **TGWEND -** Endereço
- **TGWEAS -** EnderecoAreaSep
- **TGWEAC -** EnderecoAreaConf
- **TGWEXP -** ExplosaoLote
- **TGWARS -** AreaSeparacao
- **TGWDCA -** Doca
- **TGFPEM -** EmpresaProdutoImpostos
- **TGFVOA -** HistoricoUnidadeAlternativa
- **TGFGRU -** GrupoProduto
- **TGWEXG -** EnderecoGrupoProduto
- **TGWUAS -** Separador
- **TGWFEG -** FaixaEnderecosGrupo
- **TGWEGE -** ExecutanteGrupoEnderecos
- **TGWUTE -** TipoEquipamentoUnidade
- **TGWEQP -** EquipamentoWMS
- **TGWEXU -** EnderecoUnidade
- **TGWTEC -** TarefaExecucaoColetor
- **TGFICM -** AliquotaICMS
- **TGFIPI -** AliquotaIPI
- **TGFISS -** AliquotaISS
- **TGFIMA -** AliquotaImposto
- **TGFIMC -** Imposto
- **TFPSIN -** Sindicato
- **TFPCNV -** CNV
- **TFPPRE -** RegraCalculo
- **TFPFER -** ProgramacaoFerias
- **TSIUSU -** Usuario (ignorar a coluna DTULTACESSO)

**Importante:** a tela Auditoria de Modificações não permite a edição e nem inserção de novas tabelas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003568962-Auditoria-de-Modifica%C3%A7%C3%B5es#top)
