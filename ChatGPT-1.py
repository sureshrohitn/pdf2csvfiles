from pychatgpt import Chat, Options

options = Options()

# [New] Pass Moderation. https://github.com/rawandahmad698/PyChatGPT/discussions/103
# options.pass_moderation = False

# [New] Enable, Disable logs
options.log = True

# Track conversation
options.track = True 

# Use a proxy
options.proxies = 'http://localhost:8080'

# Optionally, you can pass a file path to save the conversation
# They're created if they don't exist

# options.chat_log = "chat_log.txt"
# options.id_log = "id_log.txt"

# Create a Chat object
chat = Chat(email="email", password="password", options=options)
answer = chat.ask("How are you?")
print(answer)


from pyChatGPT import ChatGPT

session_token='eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..J8M6dSDDbDDR1k0J.JYMPrzDrOQSF4rG0EHfGlgZpny23R2ZIFU3fEnb7mf68t_IKZbOU-G_FNmM807hdL08fqaFTQ5UAOuUMr41qFQ4zWXS2Dj6u39Jex2yOlywDAM9cwPlolTlHRWuKrJ3FJSuLYCGApGmgDhH4qdj5zTuhz6HYDAvYq2qEaNasboV8y_GGtff7u0NMaYKjg4XrrYn5Lx0WqdUeOlV_JBBONoX_J42rIGCjW6ZCEaxsL2qZelIDuFSGQkGWepDyDD7wHWe4nS2ERrw4YbdkNzTW7lLy-J3f3R2I2jchnZ07YHPACZy32BlpBSGZhpRV1bp2Zas8nTbFFajbA2M4_cf8oNR20OpwRDZbWP4my2UH466R5o8MO-eumAcqP3rhxEVB090lwYQVjFFUjjXExgImf20uZlzMHA0S2sLlsgUHljfMRPA7-MSY9th5h6sGTBGoGrCtollI2RSpNHMoZKQSFzO_YKurjCgJiow5g1jQUJsss4EPoplJNbaxB3cNz0PwhyhX1oDzPZImPkUzBv3Wfs-Rdabz175NgEEyDBk8hZVCwoo7SkAVI8xhQ2J2_AywjrorXH6GD0Go9lLA6H9H5JECC6kQr8zDBC3aHxnTX-e4bgvEQoGqfgRtOOaHHARzBTQan3QhL3fqlWLa6gopAOQLDJhnNoQM-WHM_A5jX4GQvhhJ2oRbRegadARpYjILLYi7famkKKqXqweXlXqAb_3GPy4qlAzpKFlht7s83mpmd-7ph5_X260apUZh22eUAe3ZiUSPgSPPW35-B5m5yQOKkwR13NA6kMoxvnCBrKiEVjgC8AlFiGQ_QKnpTQzjdolQYj44LhOK1wmLR4fC_FKFiJyBduNRH5tDPSGQ9xBmRCAHizx4xwAVaxOjyrBDlD_DCetmd4jMSjysVtSr0q7jOKgcMN1l1svt99pMuqhnPqc5ptBcEW8POtkghP2U59gjh7Iab6eX1iTxEAHaFyXYpUjl0k10w2soC1kOO1qzpJ0pTM_BN5vjOluWE3jtquhMhrt0XDfvn2Jioar4Ad-lT__o9NNBUOaqbei-FIFCXgdvFg8JrhFa9Ts-jXAv61pg7_eYsGuNT3mlSEEhacUV0JY7Vzvlmf-bM0O3NQMxZkq3eNFuVXfLBIG35Olntrs6fCed__xWbIcnVbernqfNAeTkCPyuas6RnhL5SE25hQjvra03q63pcYIdyf57Z3j7OaszO46F1m_TJ4P9VOkqoX4VQ8HCJR3AiKiN6QlEYZqjQXoO9BZfrCkPwnasDjKUrmod2XcwdncAsaejTPJ1F8jQPq3MujXmI_HoVfjiBNbVyWjPJvPfa6d3jY-2jaEDocnW8rEJwjsMkIj1bALKwrLZZvbL_i7tAYbbgFK6qWx39Vz75ebTO-3eRKUYPCsvd3h6YeHDMSGcuUe1Llr0mNm1PuVpUvwD3RXfRHyaOSyevb5VJ5M-Veu49cE-H7PI_FeFHIx1yYR3MkIhLIxCUDpy54Ht30Xqxts0TYsyc5Wqt5onCvJ5pBH0QuPoKDi5PO--otH37mRj9YxfBwIKGIEBfrXKzSa2Y31lN9viKJtTAaEI2qzz63mNRyPXWsvsl-FbqT8YZZsYWwFVIVKeNjGy3oYItmZpDGB03irPTEafWrXld_nzufJTsl7R0WmV_VRcv1F-fZaoCI3IMwVGfMrVtgQYY-Z118ljSqQljaVB71k9xpKtRrMg5kEjuGjZoqwXak_exdTBJ3Em5SlUcEB7Fa5A8dF3w4nptsddxtY7mn4w0dG-0ob7wX1Fbf9ywhFHYCtPdGlx4geuiGeS35l1TdGOgHXr9gRjA6xtXQE-qAWE7_ZpAn1FVUp417UUZQk8W91tdCWCSAPRnscD9s-t-bVsfNPJXRzuJA6CPjX1Tp4zYsmKYR-Vnn64Z-txtKPJyJD45dohAfuySG1NyM8yFjqzuY0BnIqgUzkI1EOaRy6DncN9vLPKWdAl20zV_iiYB9AMCpxMBbf8vubIzHS0MwicBB6adQnY6lA0IvjYsLRxg4E1OLRgLiJXNw-dppGaJ2LzgdsteRObinbjvLuEnqxyerVuSuNWOOSD6qRNaEQPo52Pr5KdyWgey9xEqZQ4rEJ3Gi43bH6uLt_5fH97Z0mVDf5vH9G9KKyrxLhK0b_WPLi7ld9ffJNjL_lGU8gxZWDRz_NOorliDn43CUIFFKmF7J0sWjwTUJUD8OWBroZRH7tAt8pbJWKzIaMrLY2nXiNnkcxwmisy5wJCtacGt4CsK68n.Q3GbwCJMSceBMOVyt3o2FQ'

api=ChatGPT(session_token)

response = api.send_message("How to generate 1-200 in python")

print(ressponse["message"])
 