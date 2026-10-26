---
id: "35645520057751"
titulo: "Registro 1200: Controle de Créditos Fiscais ICMS - EFD Fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35645520057751-Registro-1200-Controle-de-Cr%C3%A9ditos-Fiscais-ICMS-EFD-Fiscal"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:24:58Z"
rotulos: ["Configuração", "Fiscal", "Ajuste da Apuração de ICMS e ICMS ST", "SEFAZ", "Crédito", "ICMS", "EFD", "Apuração", "Localização: Livros Fiscais » Arquivos » Cadastro Livro ICMS/IPI", "Passos para resolver", "Razão do erro", "Detalhe do erro"]
---

# Registro 1200: Controle de Créditos Fiscais ICMS - EFD Fiscal

**SITUAÇÃO**

REGISTRO 1200: CONTROLE DE CRÉDITOS FISCAIS - ICMS. Este registro demonstra a conta corrente dos créditos fiscais de ICMS, controlados extra-apuração. Cada UF determinará a obrigatoriedade de apresentação deste registro.

![Imagem 1: REGISTRO 1200: CONTROLE DE CRÉDITOS FISCAIS - ICMS. Este registro demonstra a conta corrente dos créditos fiscais de…](https://ajuda.sankhya.com.br/hc/article_attachments/35645506054167)

**SOLUÇÃO**

Para que o **registro seja gerado automaticamente**, é necessário que exista uma **linha de ajuste de apuração configurada**.

Os campos do **Registro 1200** são alimentados a partir da tela "**Ajuste da Apuração de ICMS e ICMS ST" exclusivamente** pela aba "**Controle Créditos Fiscais"**

- Acesse a tela **"Ajuste da Apuração de ICMS e ICMS ST" (**Livros Fiscais > Arquivos > Ajuste da Apuração de ICMS e ICMS ST) e configure conforme as orientações do artigo: [Ajuste da Apuração de ICMS e ICMS ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654-Ajuste-da-Apura%C3%A7%C3%A3o-de-ICMS-e-ICMS-ST#abacontrolecrditosfiscais:~:text=voltar%20ao%20topo%5D-,Aba%20Controle%20Cr%C3%A9ditos%20Fiscais,-Possui%20uma%20%C3%A1rea)

  **Observação:** esta tela tem como finalidade ajustar informações de apuração de ICMS relativas a **"Outros créditos e Débitos"**, **"Estornos de créditos e Débitos"** e **"Deduções"**. As informações lançadas nesta tela são utilizadas principalmente para a geração do Livro Fiscal e dos arquivos do SPED FISCAL, também conhecido como EFD-Escrituração Fiscal Digital.

  A sub-aba**"Geral"** contém informações sobre a geração do registro 1200 do EFD (campos da TGFAJN).

![Imagem 2: A sub-aba "Geral" contém informações sobre a geração do registro 1200 do EFD (campos da TGFAJN).](https://ajuda.sankhya.com.br/hc/article_attachments/35645520043671)

Além disso, é indispensável a realização do [**Registro de Apuração de ICMS**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153-Registro-de-Apura%C3%A7%C3%A3o-do-ICMS).

**Caso seja feita qualquer alteração nos ajustes, será necessário refazer e salvar o registro de apuração para que as informações sejam atualizadas.**

![Imagem 3: Caso seja feita qualquer alteração nos ajustes, será necessário refazer e salvar o registro de apuração para que as…](https://ajuda.sankhya.com.br/hc/article_attachments/35645506057751)

Após configurado, o sistema irá gerar automaticamente o Registro 1200 (Controle de Créditos Fiscais ICMS)

**Observações importantes:**

Durante a geração do SPED, o Sankhya executa uma rotina que **busca os créditos saldos em TGFAJC/TGFAJA** e gera as linhas na `TGFEFDF1200`.

- As configurações devem estar alinhadas com as operações da empresa;
- Os valores serão gerados durante a apuração do livro fiscal;
- O sistema considera tanto operações próprias quanto créditos recebidos em transferência;
- É possível controlar saldos relativos a incentivos fiscais;

Para garantir o funcionamento correto, é importante validar as configurações antes de executar a rotina de geração do livro fiscal.
