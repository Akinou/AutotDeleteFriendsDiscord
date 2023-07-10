import discord
import asyncio

# Token du bot Discord
TOKEN = 'VOTRE_TOKEN_DISCORD'

# Initialisation du client 
client = discord.Client()

# Événement déclenché 
@client.event
async def on_ready():
    print('Le bot est prêt.')

    # Récupération de la liste des amis
    friends = client.user.friends

    # Création d'une liste pour stocker les amis inactifs
    inactive_friends = []

    # Attente d'une semaine
    await asyncio.sleep(604800)  # 604800 secondes = 1 semaine

    # Vérification de l'activité des amis après une semaine
    for friend in friends:
        # Récupération du statut en ligne de l'ami
        last_online = friend.status.last_online

        # Vérification si l'ami ne s'est pas connecté depuis une semaine
        if last_online is not None and last_online < friend.created_at:
            inactive_friends.append(friend)

    # Suppression des amis inactifs
    for friend in inactive_friends:
        await friend.remove_friend()
        print(f"Ami supprimé : {friend.name}")

# Lancement du bot
client.run(TOKEN)
