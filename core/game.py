from math import (
    pi,
    sin, cos,
)

'''
单例游戏实体类
'''
class GameInstance():
    __game_instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls.__game_instance:
            cls.__game_instance = super().__new__(cls)
        return cls.__game_instance
    
    # init setting
    def __init__(self, screen_width: int, screen_height: int, map_width: int = 24, map_height: int = 24) -> None:
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.MAP_WIDTH = map_width
        self.MAP_HEIGHT = map_height
        self.GAME_MAP: list[list[int]] = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,2,2,2,2,2,0,0,0,0,3,0,3,0,3,0,0,0,1],
            [1,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,2,0,0,0,2,0,0,0,0,3,0,0,0,3,0,0,0,1],
            [1,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,2,2,0,2,2,0,0,0,0,3,0,3,0,3,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,4,0,4,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,4,0,0,0,0,5,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,4,0,4,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,4,0,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]
        self.COLOR_MAP = {
            1: (150, 0, 0),
            2: (0, 255, 0),
            3: (0, 0, 255),
            4: (255, 255, 255),
            5: (255, 0, 255),
        }
        # 长度为screen width的画线缓存区
        self.render_buffer = [
            [
                # (draw_start, draw_end)
                (0, 0),
                # rgba
                (0, 0, 0, 255)
            ] for _ in range(self.SCREEN_WIDTH)
        ]
        
        self.__init_vector()
        
    # init game vector
    def __init_vector(
        self, 
        pos_vector: tuple = (11, 11), 
        dir_vector: tuple = (0, 3), 
        plane_vector: tuple = (2, 0)
    ) -> None:
        self.pos_x, self.pos_y = pos_vector
        self.dir_x, self.dir_y = dir_vector
        self.plane_x, self.plane_y = plane_vector
        self.dir_length = (self.dir_x ** 2 + self.dir_y ** 2) ** 0.5
         
    def move(self, speed, forward: bool = True) -> None:
        if forward:
            target_x = self.pos_x + speed * self.dir_x / self.dir_length
            target_y = self.pos_y + speed * self.dir_y / self.dir_length
        else:
            target_x = self.pos_x - speed * self.dir_x / self.dir_length
            target_y = self.pos_y - speed * self.dir_y / self.dir_length
        if int(target_x) > 0 and int(target_x) < len(self.GAME_MAP[0]) - 1 and self.GAME_MAP[int(target_x)][int(self.pos_y)] == 0:
            self.pos_x = target_x
        if int(target_y) > 0 and int(target_y) < len(self.GAME_MAP) - 1 and self.GAME_MAP[int(self.pos_x)][int(target_y)] == 0:
            self.pos_y = target_y
            
    
    def rotate(self, speed, clockwise: bool = True) -> None:
        if clockwise:
            self.dir_x, self.dir_y = self.dir_x * cos(-speed) - self.dir_y * sin(-speed), self.dir_x * sin(-speed) + self.dir_y * cos(-speed)
            self.plane_x, self.plane_y = self.plane_x * cos(-speed) - self.plane_y * sin(-speed), self.plane_x * sin(-speed) + self.plane_y * cos(-speed)
        else:
            self.dir_x, self.dir_y = self.dir_x * cos(speed) - self.dir_y * sin(speed), self.dir_x * sin(speed) + self.dir_y * cos(speed)
            self.plane_x, self.plane_y = self.plane_x * cos(speed) - self.plane_y * sin(speed), self.plane_x * sin(speed) + self.plane_y * cos(speed)


    def render(self) -> list[list[list]]:
        for x in range(self.SCREEN_WIDTH):
            camera_ratio = 2 * x / self.SCREEN_WIDTH - 1
            # 计算射线方向
            ray_x, ray_y = (
                self.dir_x + camera_ratio * self.plane_x,
                self.dir_y + camera_ratio * self.plane_y
            )
            # 优化前：真实值
            # # 射线的正切值tan_ray
            # tan_ray = ray_x / ray_y
            # next_Xside_dist, next_Yside_dist = (
            #     float('inf') if ray_x ==0 else (1 + (1 / tan_ray) ** 2) ** 0.5,
            #     float('inf') if ray_y ==0 else (1 + (tan_ray) ** 2) ** 0.5,
            # )
            
            # 优化后：相对值
            next_Xside_dist, next_Yside_dist = (
                float('inf') if ray_x == 0 else abs(1 / ray_x),
                float('inf') if ray_y == 0 else abs(1 / ray_y),
            )
            map_x, map_y = int(self.pos_x), int(self.pos_y)
            Xside_dist, Yside_dist, perp_wall_dist, step_x, step_y = 0, 0, float('inf'), 0, 0
            # side = 0 -> horizonal side
            # side = 1 -> vertical side
            hit, side = 0, 0
            
            if ray_x > 0:
                step_x = 1
                Xside_dist = (map_x + 1 - self.pos_x) * next_Xside_dist
            else: 
                step_x = -1
                Xside_dist = (self.pos_x - map_x) * next_Xside_dist
            
            if ray_y > 0:
                step_y = 1
                Yside_dist = (map_y + 1 - self.pos_y) * next_Yside_dist
            else: 
                step_y = -1
                Yside_dist = (self.pos_y - map_y) * next_Yside_dist
            
            # DDA
            while hit == 0:
                if Xside_dist < Yside_dist:
                    Xside_dist += next_Xside_dist
                    map_x += step_x
                    side = 1
                else:
                    Yside_dist += next_Yside_dist
                    map_y += step_y
                    side = 0
                if self.GAME_MAP[map_x][map_y] > 0:
                    hit = 1 
            # 计算视距
            perp_wall_dist = (Yside_dist - next_Yside_dist) * self.dir_length if side == 0 else (Xside_dist - next_Xside_dist) * self.dir_length
            line_height = int(self.SCREEN_HEIGHT / perp_wall_dist) if perp_wall_dist > 0 else self.SCREEN_HEIGHT
            # line_height = self.SCREEN_HEIGHT // perp_wall_dist
            draw_start, draw_end = - line_height / 2 + self.SCREEN_HEIGHT / 2, line_height / 2 + self.SCREEN_HEIGHT / 2
            if draw_start < 0:
                draw_start = 0
            if draw_end >= self.SCREEN_HEIGHT:
                draw_end = self.SCREEN_HEIGHT - 1

            line_color = (
                * self.COLOR_MAP.get(self.GAME_MAP[map_x][map_y]),
                255 if side == 0 else 128
            )
            self.render_buffer[x][0], self.render_buffer[x][1] = (draw_start, draw_end), line_color
        
        return self.render_buffer

 
 
 
    
if __name__ == '__main__':
    pass
    game1 = GameInstance(640, 480)
    game2 = GameInstance(640, 480)
    print(id(game1), id(game2), game1 is game2)