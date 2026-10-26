---
id: "37367901608471"
titulo: "Evento S-2205 para Autônomos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37367901608471-Evento-S-2205-para-Aut%C3%B4nomos"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-22T14:12:53Z"
rotulos: ["XML", "eSocial", "Central do eSocial", "Cadastro", "Erro", "Evento S-2205", "Layout Oficial do eSocial", "TAG infoCota", "S-2205 para Autônomos", "Análise Técnica", "Autônomos"]
---

# Evento S-2205 para Autônomos

**MENSAGEM:**

Erro 1 - Campo de preenchimento obrigatório: Indicador de Preenchimento de Cota. Elemento: /eSocial/evtAltCadastral/alteracao/dadosTrabalhador/infoDeficiencia/infoCota [null]

####

#### Layout Oficial do eSocial

De acordo com o layout oficial do eSocial, o evento S-2205 (Alteração de Dados Cadastrais) é utilizado para informar alterações cadastrais tanto de:

- **Empregados CLT** (evento S-2200 – Categoria 101).
- **Trabalhadores autônomos**, quando aplicável.

Entretanto, há diferença na obrigatoriedade de determinadas informações conforme o tipo de vínculo.

####

#### Obrigatoriedade da TAG infoCota

Conforme documentação oficial do eSocial (versão 1.3):

- A **TAG** `infoCota` é **obrigatória** apenas para trabalhadores informados pelo **evento S-2200 (empregados CLT)**;
- Para **autônomos**, conforme o layout publicado, **essa informação não está definida como obrigatória** no evento S-2205.

![Imagem 1: Para autônomos , conforme o layout publicado, essa informação não está definida como obrigatória no evento S-2205.](https://ajuda.sankhya.com.br/attachments/token/2lh0hKuC8yjNWImjLSmKcdm8T/?name=%7B6B0AE2CA-330D-4F43-BD8A-2599E5E87B54%7D.png)

#### Análise Técnica

O **XML** gerado pelo **sistema Sankhya está em total conformidade** com o **layout oficial do eSocial disponibilizado pelo Governo**. As análises realizadas nos arquivos confirmam que todas as informações enviadas atendem às especificações da documentação técnica vigente.

No entanto, o eSocial está exigindo o preenchimento da TAG **infoCota** **também para trabalhadores autônomos, mesmo essa exigência não constando no layout oficial**. Essa divergência na validação do Governo é o que causa o erro no envio do evento.

#### Conclusão

O comportamento do **sistema Sankhya está correto e em total conformidade com o layout oficial do eSocial**. As informações enviadas seguem rigorosamente a documentação técnica vigente e atendem aos requisitos previstos para o evento informado.

O erro apresentado **ocorre devido a uma inconsistência entre a documentação publicada pelo eSocial e as validações atualmente aplicadas pela própria plataforma do Governo**, que exige informações além do que está formalmente definido no layout.

Dessa forma, **não há ajustes a serem realizados no sistema Sankhya**. A correção depende de **revisão da documentação ou adequação das regras de validação por parte do eSocial**, para garantir coerência e consistência no recebimento das informações.
