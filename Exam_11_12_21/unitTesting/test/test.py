from unittest import TestCase, main

from project.team import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team('Stars')

    def test_initializaton_team(self):
        expected_name = 'Stars'
        expected_members = {}

        self. assertEqual(expected_name, self.team.name)
        self.assertEqual(expected_members, self.team.members)

    def test_assert_initialization_raises_value_error_when_name_not_contains_digits(self):
        new_name = 'Stars1'
        expected = "Team Name can contain only letters!"

        with self.assertRaises(ValueError) as context:
            self.team.name = new_name

        self.assertEqual(expected, str(context.exception))

    def test_add_member_adds_correct(self):
        add_members = {'Pesho': 12, 'Kircho': 13, 'Desi': 15, 'Krasi': 14}
        expected_dict = {'Pesho': 12, 'Kircho': 13, 'Desi': 15, 'Krasi': 14}
        expected_message = "Successfully added: Pesho, Kircho, Desi, Krasi"

        self.assertEqual(expected_message, self.team.add_member(**add_members))
        self.assertEqual(expected_dict, self.team.members)

    def test_remove_member_removes_existing_member(self):
        add_members = {'Pesho': 12, 'Kircho': 13, 'Desi': 15, 'Krasi': 14}
        expected_dict = {'Kircho': 13, 'Desi': 15, 'Krasi': 14}
        expected_message = f"Member {'Pesho'} removed"

        self.team.add_member(**add_members)

        self.assertEqual(expected_message, self.team.remove_member('Pesho'))
        self.assertEqual(expected_dict, self.team.members)

    def test_remove_membe_if_member_doesnt_exist(self):
        name_to_remove = 'Nasko'
        add_members = {'Pesho': 12, 'Kircho': 13, 'Desi': 15, 'Krasi': 14}
        expected_dict = {'Pesho': 12, 'Kircho': 13, 'Desi': 15, 'Krasi': 14}
        expected_message = f"Member with name {name_to_remove} does not exist"

        self.assertEqual(expected_message, self.team.remove_member(name_to_remove))

    def test__gt__if_stars_team_is_has_more_members_than_other_team(self):
        add_members = {'Pesho': 12, 'Kircho': 13, 'Desi': 15, 'Krasi': 14}
        self.team.add_member(**add_members)
        expected = True

        other_team = Team('Other')

        self.assertEqual(expected, self.team > other_team)

    def test__qt__returns_false_when_our_team_not_greater_than_other_team(self):
        other_team = Team('Other')
        expected = False

        self.assertEqual(expected, self.team > other_team)

    def test__len__returns_the_correct_lenth(self):
        add_members = {'Pesho': 12, 'Kircho': 13, 'Desi': 15, 'Krasi': 14}
        self.team.add_member(**add_members)
        expected = 4

        self.assertEqual(expected, len(self.team))

    def test__add__if_return_new_team_with_as_sum_of_the_two(self):
        other_team = Team('Other')
        add_members = {'Pesho': 12, 'Kircho': 13, 'Desi': 15, 'Krasi': 14}
        add_members_other = {'Tencho': 10, 'Pencho': 5}
        expected_name = 'StarsOther'
        expected_members = {'Pesho': 12, 'Kircho': 13, 'Desi': 15, 'Krasi': 14, 'Tencho': 10, 'Pencho': 5}

        self.team.add_member(**add_members)
        other_team.add_member(**add_members_other)
        new_team = self.team + other_team

        self.assertEqual(expected_name, new_team.name)
        self.assertEqual(expected_members, new_team.members)

    def test__str__if_returns_proper_string(self):
        add_members = {'Pesho': 13, 'Kircho': 12}
        expected_str = f"Team name: {self.team.name}\nMember: {'Pesho'} - " \
                       f"{13}-years old\nMember: {'Kircho'} - {12}-years old"

        self.team.add_member(**add_members)
        self.assertEqual(expected_str, str(self.team))


if __name__ == '__main__':
    main()
    