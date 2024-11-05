import PlayerRow from "./PlayerRow";

export default function PlayerTable({ players }) {
  // sinon à la place de players mettre id, name, score
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Score</th>
        </tr>
      </thead>
      <tbody>
        {players?.map(
          (
            player //{player && player.map()} voir cette méthode
          ) => (
            <PlayerRow key={player.id} player={player} /> //
          )
        )}
      </tbody>
    </table>
  );
}
