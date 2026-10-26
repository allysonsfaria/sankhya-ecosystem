---
id: "27008989780887"
titulo: "Rejeição 974 - CNPJ do responsável técnico diverge do cadastrado em homologação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27008989780887-Rejei%C3%A7%C3%A3o-974-CNPJ-do-respons%C3%A1vel-t%C3%A9cnico-diverge-do-cadastrado-em-homologa%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:40:20Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "XML", "SEFAZ", "Passos para resolver", "Razão do erro", "Detalhe do erro", "rejeição 974", "CNPJ do responsável técnico diverge do cadastrado em homologação", "Erro"]
---

# Rejeição 974 - CNPJ do responsável técnico diverge do cadastrado em homologação

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/27008978106647)**MENSAGEM:**

974 - CNPJ do responsável técnico diverge do cadastrado em homologação.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27008978113815)SOLUÇÃO:**

No caso da Sankhya o responsável técnico já está cadastrado na Sefaz e a informação está presente no xml. Para confirmar, acesse o **"Portal de vendas"**, selecione a nota em questão, clique no botão **"NF-e"**, em seguida, escolha a opção **"Gerar arquivo XML de NF-e"**.

Abra o XML da nota, busque pela tag <infRespTec> e verifique que consta o nome e o CNPJ do responsável técnico da Sankhya cadastrado. Veja exemplo abaixo:

<CNPJ>**26314062000161**</CNPJ>
<xContato>**Fabio Tulio Felippe**</xContato>
<email>**marketing@sankhya.com.br**</email>
<fone>**3432390700**</fone>
<idCSRT>01</idCSRT>
<hashCSRT>Mt6caYEYd8MowcsV+LOcEpg08hs=</hashCSRT>
</infRespTec>

Ao fazer essa validação e **verificar que o nome e o CNPJ do responsável técnico da Sankhya estão de fato corretos, envie o XML para a Sefaz questionando o motivo.**

Por outro lado, se as **informações do responsável técnico não estiverem de acordo com o responsável cadastrado, faça o ajuste.**

### **(1)** Atenção para o estado do Paraná

Para o estado do **Paraná existe uma situação específica, na qual essa rejeição 974 é retornada também por outro motivo. Se houver troca do emissor, mas este não estiver devidamente cadastrado na Sefaz a rejeição 974 acontecerá.**

Assim, nos casos do estado do **Paraná, se feita a primeira verificação descrita acima** e for constatado que os dados do responsável técnico estão corretos, **a rejeição deve estar acontecendo porque o emissor não está devidamente cadastrado.** Nesse caso, confira as informações abaixo:

#### O Estado do Paraná possui Sistema Autorizador Próprio de NFC-e

O processo de credenciamento de estabelecimentos paranaenses como emissores de NFC-e deverá seguir as regras definidas na Norma de Procedimento Fiscal - NPF 101/2014.
Para o credenciamento de Sistema emissor de NFC-e, modelo 65, o fornecedor deverá efetuar os procedimentos relativos ao pedido da credencial ou de alteração da credencial de SISTEMA , conforme previsto na NPF 063/2012.
Para o contribuinte obter a autorização de uso de NFC-e deve previamente solicitar o Código de Segurança do Contribuinte - CSC, conforme previsto na NPF 100/2014.

#### Ambiente de homologação (ambiente de testes) – sem validade jurídica

Por ato de ofício da Secretaria da Fazenda, estarão automaticamente credenciados ao ambiente de homologação, independentemente de prévia autorização de uso de sistema emissor de documento fiscal, todos os estabelecimentos ativos inscritos no Cadastro de Contribuintes do ICMS – CAD/ICMS, com código de regime tributário que contemple emissão de documento fiscal.

#### Ambiente de Produção – com validade jurídica

O processo de credenciamento deve ser feito pelo contribuinte no Portal da RECEITA/PR, serviço UPD, utilizando-se do código de acesso da área restrita e da senha de representante legal previamente cadastrado e efetuando os procedimentos relativos ao cadastro ou alteração de uso de SISTEMA se for o caso, conforme previsto na NPF 063/2012.

Acesse o manual [Credenciamento do sistema para emissão de NF-e/NFCe no estado do Paraná](https://ajuda.sankhya.com.br/hc/pt-br/articles/9859583726615-Credenciamento-do-sistema-para-emiss%C3%A3o-de-NF-e-NFCe-no-estado-do-Paran%C3%A1) para maiores informações.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/27008978114967)CAUSA:**

Quando uma NF-e (modelo 55) ou NFC-e (modelo 65) é emitida e o CNPJ do responsável técnico não corresponde ao CNPJ registrado para o emitente na Sefaz regional. Pode acontecer também quando houver instabilidade na sefaz.

Além disso, para o estado do Paraná a rejeição também pode acontecer quando houver mudança de emissor e este não estiver devidamente cadastrado na Sefaz.
