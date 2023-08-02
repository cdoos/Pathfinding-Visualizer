import axios from "axios";

export async function get_visited_path(credentials) {
  try {
    const res = await axios.post("http://127.0.0.1:8000/pathfinder/", {
      rows: credentials.rows,
      columns: credentials.columns,
      obstacles: credentials.obstacles,
      start_x: credentials.start_x,
      start_y: credentials.start_y,
      target_x: credentials.target_x,
      target_y: credentials.target_y,
      algorithm: credentials.algorithm,
    });
    //   console.log(res.data);
    return res.data;
  } catch (error) {
    console.log(error);
  }
}
