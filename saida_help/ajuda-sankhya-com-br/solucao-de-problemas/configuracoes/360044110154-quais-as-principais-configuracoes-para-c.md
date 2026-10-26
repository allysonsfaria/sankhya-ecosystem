---
id: "360044110154"
titulo: "Quais as principais configurações para cálculo de ICMS Simples Nacional"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110154-Quais-as-principais-configura%C3%A7%C3%B5es-para-c%C3%A1lculo-de-ICMS-Simples-Nacional"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-24T19:11:38Z"
rotulos: ["#melhorado25032019", "Alíquotas", "Configuração", "NF-e", "Simples Nacional", "ICMS", "Impostos", "Não existe a Alíquota do SIMPLES Nacional cadastrada para a empresa", "Configurações do ICMS para CSOSN na NF-e", "Artigo atualizado KCS", "Fiscal/Contábil - KCS"]
---

# Quais as principais configurações para cálculo de ICMS Simples Nacional

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19574750050327) SOLUÇÃO:**

Para a correta geração do CSOSN nos itens da NF-e de Venda, vejamos as principais configurações:

É necessário configurar as regras de ICMS para que busque a partilha do Simples Nacional e também o respectivo CSOSN vinculado a uma "exceção de ICMS" no cadastro de Alíquotas de ICMS, dentre outras.

Passo a passo para realizar a configuração:

![Imagem 2: Acesse a tela de " Empresa " (Comercial » Preferências), aba: Propriedades](https://ajuda.sankhya.com.br/hc/article_attachments/20471387694103) Acesse a tela de "**Empresa**" (Comercial » Preferências), aba: Propriedades

- Campo: Calcula ICMS? [marcado]

![Imagem 3: Acesse a tela de " Partilha do Simples Nacional " (Comercial » Arquivo » Cadastros » Alíquotas)](https://ajuda.sankhya.com.br/hc/article_attachments/19574750058135) Acesse a tela de "**Partilha do Simples Nacional**" (Comercial » Arquivo » Cadastros » Alíquotas)

- Efetuar o cadastro da partilha seguindo a recomendação do Contador.

![Imagem 4: Acesse a tela de " Empresa " (Comercial » Preferências), aba: Simples Nacional](https://ajuda.sankhya.com.br/hc/article_attachments/19574750064151) Acesse a tela de "**Empresa**" (Comercial » Preferências), aba: Simples Nacional

- Vincular o número da Partilha de acordo com o cadastrado na rotina informada no passo 2.
- Determinar a 'Dt. Referência'.

![Imagem 5: Acesse a tela de " Empresas " (Configurações » Cadastros), aba: Naturezas, campos:](https://ajuda.sankhya.com.br/hc/article_attachments/19574750070039) Acesse a tela de "**Empresas**" (Configurações » Cadastros), aba: Naturezas, campos:

- Cód. Regime Tribut.: [Simples Nacional ou Simples Nacional excesso de sub-limite de receita bruta]
- Tipo de Partilha SN: [Configurar]

![Imagem 6: Acesse a tela de " Tipos de Operação - TOP " (Comercial » Arquivo » Cadastros), aba: Impostos](https://ajuda.sankhya.com.br/hc/article_attachments/19574750070551) Acesse a tela de "**Tipos de Operação - TOP**" (Comercial » Arquivo » Cadastros), aba: Impostos

- Calculo de ICMS, IPI e ISS [configurado de acordo]
- Tem ICMS? [marcado]
- Classificação ICMS [Usar do Parceiro]
- Calcular DIFAL Partilhado? (Caso seja operação interestadual para Consumidor Final Não Contribuinte) [marcado]

![Imagem 7: Acesse a tela de " Parceiros " (Configurações » Cadastros), aba: Fiscal](https://ajuda.sankhya.com.br/hc/article_attachments/19574723727383) Acesse a tela de "**Parceiros**" (Configurações » Cadastros), aba: Fiscal

- Classificação ICMS [Configurar de acordo com orientação do contador]

![Imagem 8: Acesse a tela de " Produtos" (Configurações » Cadastros), aba: ' Impostos ' ou ' Impostos/Informações por Empresa '](https://ajuda.sankhya.com.br/hc/article_attachments/19574750081815) Acesse a tela de "**Produtos"** (Configurações » Cadastros),  aba: 'Impostos' ou 'Impostos/Informações por Empresa'

- Verificar se está marcado para 'Calcular ICMS'
- Verificar se esta marcado a opção 'Calcular DIFAL ?' (Caso seja operação interestadual para Consumidor Final Não Contribuinte)

![Imagem 9: Acesse a tela de " Alíquotas de ICMS " (Comercial » Arquivo » Cadastros » Alíquotas) De acordo com a movimentação da…](https://ajuda.sankhya.com.br/hc/article_attachments/19574723742871) Acesse a tela de "**Alíquotas de ICMS**" (Comercial » Arquivo » Cadastros » Alíquotas)

De acordo com a movimentação da nota, pesquisar a regra de ICMS e na aba: 'Simples Nacional', informar o 'CSOSN'.

**Observação:**

Existe uma combinação entre CST x CSOSN, que pode ser verificada com o contador da empresa, para que não surjam rejeições ao confirmar a nota.

![Imagem 10: Após os ajustes redigitar Empresa/Parceiro da Nota e confirmar novamente a nota.](https://ajuda.sankhya.com.br/hc/article_attachments/19574723742871) Após os ajustes redigitar Empresa/Parceiro da Nota e confirmar novamente a nota.

 **Observações:**

**Obs.1:** Parâmetro: **VALPARTSNUNICA -Valida partilha do Simples Nac. mesmo sendo única?**

Descrição: Quando o parâmetro estiver desligado, o sistema continua com o comportamento de não validar a partilha quando houver apenas uma partilha informada nas preferências da empresa. Quando ligado o parâmetro, a validação passa ocorrer mesmo com apenas uma partilha.

- Erros relacionados a configuração incorreta da Partilha do Simples Nacional:

Erro: [Fast Service]

Processo: Cálculo de ICMS.
Nro.Único: 1500012010. Empresa: 8. Produto: 47. Usado Como: V. Tipo de Partilha: 2. Data: 28/10/2019.
Não existe a Alíquota do SIMPLES Nacional cadastrada para a empresa.
Cadastre-a em Arquivos/Cadastros/Alíquotas/Partilha SIMPLES Nacional e depois relacione a mesma nas preferências da empresa, aba SIMPLES Nacional.

**Obs.2:** Caso a opção: "Escriturar valor de ICMS de entrada para Empresa Simples?", na tela "Comercial > Preferências > Empresa" esteja marcada, o sistema não preencherá o CSOSN nos itens.

**Obs.3:** Atenção quanto ao campo: "Tem convênio Simples Nacional no Estado", pois se a empresa for do Simples Nacional, com o campo marcado, ela também será simples no seu estado. Se desmarcar o campo, ela será considerada regime normal dentro do seu próprio estado.
