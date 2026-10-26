---
id: "36292338574743"
titulo: "Especificações sobre a emissão de NFS-e no padrão nacional"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36292338574743-Especifica%C3%A7%C3%B5es-sobre-a-emiss%C3%A3o-de-NFS-e-no-padr%C3%A3o-nacional"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Emissões em conformidade com o Padrão Nacional"
atualizado_em: "2026-09-28T11:36:35Z"
rotulos: ["Configuração", "Impostos", "Preferências", "Prefeituras", "NFS-e", "Especificações sobre a emissão de NFS-e no padrão nacional", "Documentos Eletrônicos"]
---

# Especificações sobre a emissão de NFS-e no padrão nacional

**Versão Mínima**: 4.35b141
**Caminho de Acesso**: Menu Principal > Preferências > Empresa > Aba Documentos Fiscais Eletrônicos > NFSe

---

## Sumário

- [Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/36292338574743-Especifica%C3%A7%C3%B5es-sobre-a-emiss%C3%A3o-de-NFS-e-no-padr%C3%A3o-nacional#h_01K7FGMW649QPQ49JJZFN8HK2S)
  - [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/36292338574743-Especifica%C3%A7%C3%B5es-sobre-a-emiss%C3%A3o-de-NFS-e-no-padr%C3%A3o-nacional#h_01K7FGMW659CDSXN3H2A5CSM52)
  - [2. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/36292338574743-Especifica%C3%A7%C3%B5es-sobre-a-emiss%C3%A3o-de-NFS-e-no-padr%C3%A3o-nacional#h_01K7FGMW6G2R66V6PWDSQE1V8W)
  - [3. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/36292338574743-Especifica%C3%A7%C3%B5es-sobre-a-emiss%C3%A3o-de-NFS-e-no-padr%C3%A3o-nacional#h_01K7FGMW7JBHJ5DTVXAYJCZQNN)
  - [4. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/36292338574743-Especifica%C3%A7%C3%B5es-sobre-a-emiss%C3%A3o-de-NFS-e-no-padr%C3%A3o-nacional#h_01K7FGMW7PGVHCQHCQA5E0Z4WF)
  - [5. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/36292338574743-Especifica%C3%A7%C3%B5es-sobre-a-emiss%C3%A3o-de-NFS-e-no-padr%C3%A3o-nacional#h_01K7FGMW7WXD74PB7C21EC91GV)
- [FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/36292338574743-Especifica%C3%A7%C3%B5es-sobre-a-emiss%C3%A3o-de-NFS-e-no-padr%C3%A3o-nacional#h_01K7FGMW81P8766VED8EMW6GPF)
- [Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/36292338574743-Especifica%C3%A7%C3%B5es-sobre-a-emiss%C3%A3o-de-NFS-e-no-padr%C3%A3o-nacional#h_01K7FGMW8E6BXRY0SHBRCMZ10E)

---

## Descrição e Usabilidade

---

### 1. Descrição da Funcionalidade

Este artigo vai te ajudar a realizar a configuração do sistema Sankhya para emitir a Nota Fiscal de Serviços Eletrônica (NFS-e) no padrão nacional. O processo garante que a empresa esteja conforme as exigências legais, centralizando a configuração e validação dos requisitos necessários para a emissão correta do documento fiscal.

---

### 2. Jornada de Uso

1. **Verifique a disponibilidade municipal**
   Antes de qualquer configuração, confirme junto à prefeitura se o ambiente municipal está apto a receber e processar NFS-e no padrão nacional. Se o ambiente estiver indisponível, a emissão não será possível, mesmo com o sistema configurado.
2. **Preencha os campos obrigatórios**
   Para utilizar a funcionalidade de emissão da NFS-e no Padrão Nacional, é necessário configurar o sistema em duas etapas principais: ativar a função e ajustar os campos de série e numeração.

(1)** Ativação da Funcionalidade**

- Acesse **Menu Principal** > **Preferências** > [**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) **>** [**Documentos Fiscais Eletrônicos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos) **>**[**NFS-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) e ative a opção **"Emitir NFS-e Padrão Nacional"**, que define automaticamente o prefixo da série.
- Ao ativar esta opção, o sistema passa a utilizar o layout do Padrão Nacional para a emissão de NFS-e, e o parâmetro CODIBGENFSENAC será ignorado para a sua empresa.

(1)** Configuração da Série e Numeração (Campos Obrigatórios)**

Após a ativação, você deve garantir que os campos de série e numeração estejam corretamente preenchidos para formar o sequencial exigido pelo Padrão Nacional.

| **Campo de Entrada no Sistema** | **Local de Configuração** | **Formato e Regra** |
| --- | --- | --- |
| Prefixo Série NFS-e Padrão Nacional | **Preferências** > [**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) **>** [**Documentos Fiscais Eletrônicos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos) **>**[**NFS-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Geral) (definido ao ativar a opção acima) | 2 dígitos (ex.: 10). |
| Série da Nota | [TOP (Tipo de Operação)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) > Botão Outras Opções > [Controle de Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao) | 3 dígitos (ex.: 001). Deve ser configurada para ser concatenada. |

(1)** Como a Série Final é Formada (5 Dígitos):**

A **Série NFS-e Padrão Nacional** (o número que aparecerá na nota, entre 10000 e 49999) é o resultado da **concatenação** do Prefixo da Empresa (2 dígitos) com a Série da Nota (definida na TOP, 3 dígitos).

- **Fórmula:** {Prefixo (Empresa)} + {Série (TOP)} = {Série Final Padrão Nacional}
- **Exemplo:** {Prefixo} 10 + {Série } 001 = {Série Final } 10001

Portanto, **é essencial preencher corretamente os campos de Prefixo e Série (na TOP)** para assegurar que a formação da Série NFS-e Padrão Nacional esteja em conformidade.

Além disso, é importante ressaltar que o **"Cód. Trib. Município NFS-e"**, no cadastro de [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), precisa ser atualizado para o seguinte formato: 01.02.01

Para o portal nacional espera-se que o campo seja preenchido com o item da lista de serviço acrescido 01 no final.

3. **Ajuste a retenção de ISS, se aplicável**
   - No caso de retenção de ISS, preencha o campo **“Tipo de Retenção do ISS”** (aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abaimpostos) da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)) com uma das opções: 
     1. Não Retido;
     2. Retido pelo Tomador;
     3. Retido pelo Intermediário.
   - Se não houver retenção, o sistema preencherá automaticamente como **“Não Retido”**.
4. **Regra específica para UF e Simples Nacional**
   - Se a UF da empresa estiver no parâmetro **CODIBGENFSENAC** e o regime de apuração do Simples Nacional estiver definido, o prefixo deve ser entre 00 e 49. Caso contrário, o sistema exibirá uma mensagem de alerta.
5. **Configure o grupo de Comércio Exterior, se o tomador estiver no exterior**
   - Na prestação de serviços para tomadores estrangeiros, o layout nacional exige um grupo de informações de comércio exterior. Parametrize os campos no [Contrato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774) e dos cadastros de [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553), [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494) e [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), e complete os dados de movimentação de bens na aba [Comércio Exterior do rodapé da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01M3KVWJSRXXEXMMJPHNTY2HV6).
   - Para saber mais, acesse o link [Emissão de NFS-e no padrão nacional para tomadores no exterior](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799).
6. **Finalize e emita a NFS-e**
   Com todas as configurações corretas, o sistema gerará o XML da NFS-e conforme o layout do padrão nacional.

---

### 3. Pontos de Atenção

- A indisponibilidade do ambiente municipal impede a emissão da NFS-e, independentemente da configuração do sistema.
- Os campos obrigatórios devem ser preenchidos exatamente conforme o padrão exigido.
- A configuração é válida para empresas de qualquer regime tributário: Simples Nacional, Lucro Presumido ou Lucro Real.
- O prefixo da série deve respeitar as regras específicas para UF e Simples Nacional.

---

### 4. Dicas de Usabilidade

- Consulte a ajuda do sistema na sessão **Preferências** > [**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) para detalhes sobre os parâmetros.
- Utilize a exportação para planilhas para validar os dados antes da emissão.
- Sempre confirme com a prefeitura sobre atualizações ou mudanças no ambiente municipal.
- Em caso de dúvidas sobre retenção de ISS, verifique a aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abaimpostos) da **Central de Vendas**.

---

### 5. Casos de Uso

✅ **Exemplo Real:**
Empresa do Simples Nacional, com ambiente municipal disponível, ativa a opção “Emitir NFS-e Padrão Nacional”, preenche os campos obrigatórios e emite a nota com sucesso.

❌ **Erro Comum:**
Usuário tenta emitir NFS-e sem verificar a disponibilidade municipal ou sem preencher corretamente o prefixo da série, resultando em erro de validação.

---

## FAQ – Dúvidas Frequentes

1. **O que acontece se o ambiente municipal estiver indisponível?**
   A emissão da NFS-e não será possível, mesmo que o sistema Sankhya esteja corretamente configurado.
2. **Posso usar o padrão nacional em qualquer regime tributário?**
   Sim, a configuração é válida para Simples Nacional, Lucro Presumido e Lucro Real.
3. **Quais campos são obrigatórios para emissão no padrão nacional?**
   Prefixo da Série NFS-e Padrão Nacional, Série da Nota e Série NFS-e Padrão Nacional.
4. **Como configurar a retenção de ISS?**
   Preencha o campo **“Tipo de Retenção do ISS”** na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abaimpostos) da Central de Vendas. Se não houver retenção, o sistema preenche automaticamente como **“Não Retido”**.
5. **O parâmetro CODIBGENFSENAC ainda é utilizado?**
   Não, ao ativar a opção nacional, esse parâmetro é ignorado para a empresa.
6. **O que fazer se receber mensagem sobre o prefixo da série?**
   Verifique se a UF da empresa e o regime de apuração do Simples Nacional estão corretos e se o prefixo está entre 80 e 89.

---

## Artigos Relacionados

- [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos:~:text=Ao%20marcar%20a%20op%C3%A7%C3%A3o%20%22Emitir%20NFS%2De%20Padr%C3%A3o%20Nacional%22%2C)
- [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)
- [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
