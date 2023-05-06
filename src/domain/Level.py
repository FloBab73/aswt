from src.domain.BlockType import BlockType


class Level:

    def __init__(self, event_handler, static_blocks, enemies, player):
        self.event_handler = event_handler
        self.static_blocks = static_blocks
        self.enemies = enemies
        self.player = player
        self.blocks_without_player = self.static_blocks + self.enemies
        self.blocks_without_enemies = self.static_blocks + [self.player]
        self.all_blocks = self.static_blocks + [self.player] + self.enemies

        self.door_open = False

        event_handler.add(event_handler.Events.PICKUP_HEALTH, player.modify_health)
        event_handler.add(event_handler.Events.PICKUP_KEY, player.find_key)
        event_handler.add(event_handler.Events.DAMAGE, player.modify_health)
        event_handler.add(event_handler.Events.REMOVE_BLOCK, self.remove_block)
        event_handler.add(event_handler.Events.KILL_ENEMY, self.remove_enemy)
        event_handler.add(event_handler.Events.DOOR, self.try_open_door)
        self.keys = 0
        for block in static_blocks:
            if block.block_type == BlockType.ITEM_KEY:
                self.keys += 1

    def remove_block(self, x, y):
        for block in self.static_blocks:
            if block.x == x and block.y == y:
                self.static_blocks.remove(block)
                break
        self.update_blocks()

    def remove_enemy(self, x, y):
        for block in self.enemies:
            if block.x == x and block.y == y:
                self.enemies.remove(block)
                break
        self.update_blocks()

    def update_blocks(self):
        self.blocks_without_player.clear()
        self.blocks_without_player.extend(self.static_blocks + self.enemies)
        self.blocks_without_enemies.clear()
        self.blocks_without_enemies.extend(self.static_blocks + [self.player])
        self.all_blocks.clear()
        self.all_blocks.extend(self.static_blocks + [self.player] + self.enemies)

    def try_open_door(self):
        if self.player.keys == self.keys and not self.door_open:
            self.door_open = True
            self.event_handler.remove(self.event_handler.Events.PICKUP_HEALTH, self.player.modify_health)
            self.event_handler.remove(self.event_handler.Events.PICKUP_KEY, self.player.find_key)
            self.event_handler.remove(self.event_handler.Events.DAMAGE, self.player.modify_health)
            self.event_handler.remove(self.event_handler.Events.REMOVE_BLOCK, self.remove_block)
            self.event_handler.remove(self.event_handler.Events.KILL_ENEMY, self.remove_enemy)
            self.event_handler.remove(self.event_handler.Events.DOOR, self.try_open_door)
            self.event_handler(self.event_handler.Events.QUIT_LEVEL)
            print("********* Door Open, Game Over ************")

