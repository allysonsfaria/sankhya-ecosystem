---
id: "36939875156631"
titulo: "Configurações Gateway - Tratamento do erro “Cannot read property 'descrição' of undefined” / “Falha ao acessar o EIP Sankhya”"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36939875156631-Configura%C3%A7%C3%B5es-Gateway-Tratamento-do-erro-Cannot-read-property-descri%C3%A7%C3%A3o-of-undefined-Falha-ao-acessar-o-EIP-Sankhya"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:22:08Z"
rotulos: ["Configuração", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Endereço Sankhya", "Gateway", "Cannot read", "Configurações de Gateway", "Valide a URL", "Acesso Externo", "Sankhya Om", "Comunicação"]
---

# Configurações Gateway - Tratamento do erro “Cannot read property 'descrição' of undefined” / “Falha ao acessar o EIP Sankhya”

**MENSAGEM:**

**Erro 1:** “Falha ao acessar o EIP Sankhya. Verifique se a URL informada no campo 'Endereço Sankhya' está correta e possui acesso à internet.”

**Erro 2:** “Cannot read property 'descrição' of undefined”

**SITUAÇÃO:**

Ao acessar a tela **''**[**Configurações de Gateway**](https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway)**'' (**Configurações » Avançado » Configurações Gateway), o sistema pode impedir a gravação de alterações ou criação de novos registros apresentando os erros acima.

**SOLUÇÃO:**

Para normalizar a comunicação do Gateway, siga os passos abaixo:

(1)** Valide a URL e o Acesso Externo**

- **Mesmo Endereço de Acesso**

Certifique-se de que você está conectado ao Sankhya OM utilizando exatamente a **mesma URL** que foi preenchida no campo "Endereço Sankhya".

- **Teste de Acesso Externo**

Acesse a mesma URL a partir de uma rede externa (como o 4G do celular). Se a URL não carregar fora da rede da empresa, o Gateway não conseguirá completar a conexão.

- **VPN**

O Gateway **não é compatível com VPN**. A conexão deve ser direta via HTTP/HTTPS.

**Exemplos**:

- Correto: `https://empresa.sankhya.com.br`
- Incorreto: `http://localhost:8080` ou `http://192.168.x.x`

(2)** Liberação de IPs no Firewalll**

Verifique se o firewall do servidor de aplicação permite conexões de saída para os IPs da Sankhya. Caso contrário, adicione-os manualmente nas regras de exceção:

| Ambiente | IPs para Liberação |
| --- | --- |
| Produção | 144.22.228.211 e 144.22.217.141 |
| Sandbox (Testes) | 150.230.86.234 e 144.22.173.39 |

##### **(3)** Ajuste do endereço Sankhya

- O campo **“Endereço Sankhya”** é preenchido automaticamente com o endereço usado para acessar o Sankhya OM.
- Em muitos casos, ele pode ser local (localhost, IP interno, servidor privado), o que impede a validação externa.
- Altere para um domínio público ou IP externo acessível.

**OBSERVAÇÃO:** Caso utilize **balanceamento**, **proxy reverso** ou **subdomínios externos**, informe o **endereço público** configurado para acesso externo ao Sankhya Om.

Se a aplicação estiver em rede restrita, certifique-se de que o endereço do Gateway esteja liberado no firewall:

Produção:

- **144.22.228.211**
- **144.22.217.141**

Sandbox (testes):

- **150.230.86.234**
- **144.22.173.39**

**CAUSA:**

O erro ocorre quando o sistema não consegue validar ou salvar as informações na tela ''Configurações de Gateway'', geralmente devido a problemas de comunicação ou configuração do campo **Endereço Sankhya**.

A tela possui validações específicas: o endereço precisa ser acessível externamente, ter formato válido (domínio ou IP público) e estar vinculado ao cliente correto. Além disso, não pode haver falhas internas de configuração ou dados incompletos. Quando alguma dessas condições não é atendida, surgem erros como **“Cannot read property 'descrição' of undefined”** ou **falha ao acessar o EIP Sankhya**.

As principais causas incluem:

- **Endereço Sankhya incorreto:** uso de localhost, IP interno ou servidor privado que não é acessível externamente.
- **Firewall bloqueando:** impede que o Gateway se comunique com os servidores da Sankhya.
- **VPN ativa:** o Gateway não funciona via VPN; precisa de conexão direta HTTP/HTTPS.
- **Falha de resposta do servidor:** quando o Sankhya não envia os dados necessários, a configuração não é concluída.
