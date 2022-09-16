
class Unit:

    def move(self, field,
             x_coordinate: int,
             y_coordinate: int,
             direction,
             flight: bool,
             crawl: bool,
             initial_speed=1):

        if flight and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        """
        Направление нашего движения: 'UP', 'DOWN', 'LEFT', 'RIGHT'
        """

        if flight:  # реализация логики для состояния 'Полет'
            initial_speed *= 1.2
            if direction == 'UP':
                new_y = y_coordinate + initial_speed
                new_x = x_coordinate
            elif direction == 'DOWN':
                new_y = y_coordinate - initial_speed
                new_x = x_coordinate
            elif direction == 'LEFT':
                new_y = y_coordinate
                new_x = x_coordinate - initial_speed
            elif direction == 'RIGHT':
                new_y = y_coordinate
                new_x = x_coordinate + initial_speed

        if crawl:  # реализация логики для состояния 'Ползти'
            initial_speed *= 0.5
            if direction == 'UP':
                new_y = y_coordinate + initial_speed
                new_x = x_coordinate
            elif direction == 'DOWN':
                new_y = y_coordinate - initial_speed
                new_x = x_coordinate
            elif direction == 'LEFT':
                new_y = y_coordinate
                new_x = x_coordinate - initial_speed
            elif direction == 'RIGHT':
                new_y = y_coordinate
                new_x = x_coordinate + initial_speed

            field.set_unit(x=new_x, y=new_y, unit=self)
