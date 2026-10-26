---
id: "39286730158615"
titulo: "Cadastro de Alíquota CBS e IBS - Não exibe CST e Código de Classificação Tributária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39286730158615-Cadastro-de-Al%C3%ADquota-CBS-e-IBS-N%C3%A3o-exibe-CST-e-C%C3%B3digo-de-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-09-11T19:42:29Z"
rotulos: ["Configuração", "Atualização", "Impostos", "Artigo criado KCS", "Alíquotas de CBS", "Alíquotas de IBS", "Fiscal/Contábil - KCS"]
---

# Cadastro de Alíquota CBS e IBS - Não exibe CST e Código de Classificação Tributária

## MENSAGEM

Os campos **"CST"** e **"Código de Classificação Tributária"** não são exibidos na tela de cadastro de alíquotas de IBS ou CBS.

## SITUAÇÃO

Ao acessar as telas **"Alíquotas de IBS"** (Livros Fiscais >> Cadastros >> Alíquotas de IBS) ou **"Alíquotas de CBS"** (Livros Fiscais >> Cadastros >> Alíquotas de CBS), na guia **"Tributação"**, o usuário não consegue visualizar ou preencher os campos **"CST"** e **"Código de Classificação Tributária"** no grupo **"Dados de Tributação".**

## SOLUÇÃO

Para resolver esta situação, siga os passos abaixo:

**(1)** Acesse a tela **"Alíquotas de IBS"** ou **"Alíquotas de CBS"** (Livros Fiscais >> Cadastros >> Alíquotas de IBS ou Livros Fiscais >> Cadastros >> Alíquotas de CBS).

**(2)** Navegue até a guia **"Tributação"**. 

**(3)** Localize o grupo **"Dados de Tributação"**, que deve conter os campos **"CST"** e **"Código de Classificação Tributária"**.

**(4)** Verifique se os campos estão visíveis e habilitados para preenchimento. Caso não estejam, seleciona a seguinte opção: "Mais opções" >> "Atualizar tabelas RTC". 

![Imagem 1: (1) Acesse a tela "Alíquotas de IBS" ou "Alíquotas de CBS" (Livros Fiscais >> Cadastros >> Alíquotas de IBS ou Livros…](https://ajuda.sankhya.com.br/hc/article_attachments/39443832786839)

O job passa a ser executado de forma imediata e com recorrência mensal, substituindo a periodicidade diária adotada até janeiro. Essa opção está disponível a partir da versão 5.30.0 do Livros Fiscais e permite forçar a atualização das tabelas de IBS e CBS de forma imediata, sendo eficaz para correções pontuais como a ocorrida em seu ambiente. 

 Ressaltamos, no entanto, que essa funcionalidade não deve ser utilizada com frequência, pois existe uma limitação de uso (**uma execução a cada 7 dias**) e sua aplicação é recomendada apenas para casos excepcionais, como este. Em condições normais, as atualizações são realizadas automaticamente pelo job mensal, não sendo necessária intervenção manual.

**(5)** Preencha obrigatoriamente os campos **"CST"** e **"Código de Classificação Tributária"**, selecionando valores válidos das tabelas **"TLFCSTIC"** e **"TLFCLASTRIBIC"**, respectivamente.

## CAUSA

A ausência dos campos **"CST"** e **"Código de Classificação Tributária"** pode ocorrer devido a:

- **Configuração incorreta da tela**: o grupo **"Dados de Tributação"** pode não estar configurado corretamente na guia **"Tributação"**.
- **Versão desatualizada do sistema**: versões anteriores podem não conter a estrutura completa dos campos obrigatórios para a reforma tributária.
- As tabelas **TLFCLASTRIBIC** e **TLFCSTIC** não foram devidamente alimentadas, o que está impedindo o cadastramento das alíquotas de **IBS** e **CBS**.

**OBSERVAÇÃO:** Esse comportamento pode ocorrer em bases novas, nas quais o Job responsável por alimentar as tabelas de RTC (`TLFCLASTRIBIC` e `TLFCSTIC`) ainda não foi executado. Esse Job é processado automaticamente uma vez por mês — em ambientes recém-implantados, pode haver um intervalo até a primeira execução. Nesses casos, use a opção **"Atualizar tabelas RTC"** em **''Mais opções''**, na tela de Alíquotas de IBS/CBS) para forçar a atualização imediatamente.
